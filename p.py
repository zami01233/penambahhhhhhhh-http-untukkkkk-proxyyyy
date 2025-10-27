# ==========================================
#  Auto Tambah Prefix Proxy
#  Format: username:password@ip:port â†’ http://username:password@ip:port
#  Output: proxy.txt
# ==========================================

import os

def tambah_prefix_proxy(input_file="proxy.txt"):
    if not os.path.exists(input_file):
        print(f"File '{input_file}' tidak ditemukan, membuat baru...")
        open(input_file, 'w').close()
        return

    # Baca semua baris dari file
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    updated_lines = []
    for line in lines:
        # Hapus protokol yang tidak diinginkan
        if line.startswith(("http://", "https://", "socks4://", "socks5://")):
            line = line.split("://", 1)[-1]
        # Tambahkan http:// jika belum ada
        line = f"http://{line}"
        updated_lines.append(line)

    # Simpan hasilnya ke file yang sama (proxy.txt)
    with open(input_file, 'w') as f:
        f.write("\n".join(updated_lines))

    print(f"âœ… Prefix berhasil ditambahkan untuk {len(updated_lines)} proxy.")
    print(f"ðŸ“ File disimpan: {input_file}")


if __name__ == "__main__":
    tambah_prefix_proxy()
