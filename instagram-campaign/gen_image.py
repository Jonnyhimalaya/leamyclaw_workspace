#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai>=1.0.0",
#     "pillow>=10.0.0",
# ]
# ///
"""Generate images using available Gemini/Imagen models with fallback."""

import argparse
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", "-p", required=True)
    parser.add_argument("--filename", "-f", required=True)
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    from google import genai
    from google.genai import types
    from PIL import Image as PILImage
    from io import BytesIO

    client = genai.Client(api_key=api_key)
    output_path = Path(args.filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Models to try in order of preference
    models_to_try = [
        "imagen-4.0-generate-001",
        "imagen-4.0-fast-generate-001",
        "gemini-2.5-flash-image",
        "gemini-3.1-flash-image-preview",
        "gemini-3-pro-image-preview",
    ]

    for model_name in models_to_try:
        print(f"Trying model: {model_name}...")
        try:
            if model_name.startswith("imagen"):
                response = client.models.generate_images(
                    model=model_name,
                    prompt=args.prompt,
                    config=types.GenerateImagesConfig(
                        number_of_images=1,
                        aspect_ratio="1:1",
                    )
                )
                if response.generated_images:
                    img_data = response.generated_images[0].image.image_bytes
                    image = PILImage.open(BytesIO(img_data))
                    image.convert('RGB').save(str(output_path), 'PNG')
                    full_path = output_path.resolve()
                    print(f"\nImage saved: {full_path}")
                    print(f"MEDIA: {full_path}")
                    return
                else:
                    print(f"No images returned from {model_name}", file=sys.stderr)
                    continue
            else:
                response = client.models.generate_content(
                    model=model_name,
                    contents=args.prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=["TEXT", "IMAGE"],
                        image_config=types.ImageConfig(image_size="1K")
                    )
                )
                image_saved = False
                for part in response.parts:
                    if part.inline_data is not None:
                        image_data = part.inline_data.data
                        if isinstance(image_data, str):
                            import base64
                            image_data = base64.b64decode(image_data)
                        image = PILImage.open(BytesIO(image_data))
                        image.convert('RGB').save(str(output_path), 'PNG')
                        image_saved = True
                if image_saved:
                    full_path = output_path.resolve()
                    print(f"\nImage saved: {full_path}")
                    print(f"MEDIA: {full_path}")
                    return
                else:
                    print(f"No image parts in response from {model_name}", file=sys.stderr)
                    continue
        except Exception as e:
            print(f"Model {model_name} failed: {e}", file=sys.stderr)
            continue

    print("All models failed.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
