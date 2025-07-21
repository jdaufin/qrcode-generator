# generate_qr.py
import qrcode
import argparse
from pathlib import Path

def generate_qr(url: str, output: Path):
    qr = qrcode.make(url)
    output.parent.mkdir(parents=True, exist_ok=True)
    qr.save(output)
    print(f"✅ QR Code généré : {output}")

def main():
    parser = argparse.ArgumentParser(description="Génère un QR code à partir d'une URL.")
    parser.add_argument("url", help="URL à encoder")
    parser.add_argument("-o", "--output", default="qrcode.png", help="Chemin du fichier PNG de sortie")
    args = parser.parse_args()

    generate_qr(args.url, Path(args.output))

if __name__ == "__main__":
    main()

