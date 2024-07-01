import requests

# URL API Random User
url = 'https://randomuser.me/api'

# Parameter untuk mendapatkan 10 hasil
params = {
    'results': 10
}

# Mengirim permintaan GET ke API
response = requests.get(url, params=params)

# Mengecek status kode dari respons
if response.status_code == 200:
    # Mengubah respons menjadi JSON
    data = response.json()
    # Mengambil daftar pengguna dari data JSON
    users = data['results']
    
    # Implementasi algoritma selection sort untuk mengurutkan pengguna berdasarkan umur
    def selection_sort(users):
        for i in range(len(users)):
            min_idx = i
            for j in range(i + 1, len(users)):
                if users[min_idx]['dob']['age'] > users[j]['dob']['age']:
                    min_idx = j
            users[i], users[min_idx] = users[min_idx], users[i]
        return users
    
    # Mengurutkan pengguna menggunakan selection sort
    sorted_users = selection_sort(users)
    
    # Menampilkan informasi setiap pengguna
    for i, user in enumerate(sorted_users):
        gender = user['gender']
        first = user['name']['first']
        last = user['name']['last']
        title = user['name']['title']
        age = user['dob']['age']
        country = user['location']['country']

        print('     ')
        print(f'Pengguna {i + 1}')
        print(f'Nama : {title} {first} {last}')
        print(f'Umur : {age}')
        print(f'Asal : {country}')
        
        if gender == 'male':
            print('Jenis Kelamin : Laki-laki')
        else:
            print('Jenis Kelamin : Perempuan')
else:
    # Jika permintaan gagal, tampilkan kode status
    print(f'Gagal mengambil data: {response.status_code}')
