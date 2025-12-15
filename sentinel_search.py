# File: sentinel_search.py (Logika Algoritma)

# List global untuk menyimpan riwayat langkah
HISTORY = []

def sentinel_search(data_list, target):
    """
    Mengimplementasikan Sentinel Search dan mencatat setiap langkah di HISTORY.
    Mengembalikan index jika ditemukan, atau -1 jika tidak ditemukan.
    """
    global HISTORY
    HISTORY = []
    
    arr = data_list[:]
    n = len(arr)
    
    # Simpan nilai terakhir yang asli (penting untuk dikembalikan)
    last_value = arr[n - 1]
    
    # 1. Tempatkan nilai target (sentinel) di posisi terakhir
    arr[n - 1] = target
    
    # Catat status inisialisasi sentinel
    HISTORY.append({
        'array': arr[:],
        'target': target,
        'index': n - 1, # Menyorot posisi sentinel
        'status': 'Inisialisasi',
        'action': f'Menempatkan Nilai Sentinel ({target}) pada Indeks terakhir ({n-1}). Nilai asli di sini adalah {last_value}.'
    })
    
    i = 0
    # 2. Mulai pencarian
    # Loop HANYA memiliki satu perbandingan: arr[i] == target
    while arr[i] != target:
        # Catat langkah pengecekan sebelum perbandingan
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'index': i,
            'status': 'Mengecek',
            'action': f'Mengecek Indeks {i} (Nilai: {arr[i]})'
        })
        i += 1
        
        # Jika i sudah mencapai posisi sentinel, ini akan dicatat di langkah berikutnya,
        # dan loop akan berhenti karena arr[i] == target.
    
    # 3. Pulihkan nilai asli di posisi terakhir
    arr[n - 1] = last_value
    
    # 4. Tentukan hasil
    if i < n - 1:
        # Ditemukan di dalam array asli
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'index': i,
            'status': 'Ditemukan',
            'action': f'Nilai {target} DITEMUKAN pada Indeks {i} (sebelum posisi Sentinel)!'
        })
        return i, HISTORY
        
    elif i == n - 1 and last_value == target:
        # Ditemukan di posisi terakhir (yang kebetulan adalah nilai target asli)
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'index': i,
            'status': 'Ditemukan',
            'action': f'Nilai {target} DITEMUKAN pada Indeks {i}. (Nilai asli di posisi Sentinel).'
        })
        return i, HISTORY
        
    else:
        # Ditemukan di posisi sentinel, tapi nilai aslinya BUKAN target
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'index': i,
            'status': 'Tidak Ditemukan',
            'action': f'Pencarian mencapai Sentinel. Nilai {target} TIDAK DITEMUKAN dalam array asli.'
        })
        # Catat status selesai setelah semua selesai
        HISTORY.append({
            'array': arr[:],
            'target': target,
            'index': -1,
            'status': 'Selesai',
            'action': f'Selesai. Nilai {target} tidak ditemukan dalam array.'
        })
        return -1, HISTORY
