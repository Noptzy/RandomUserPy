import requests

url = 'https://randomuser.me/api'
    
hasil = {
    'results': 10
}

response = requests.get(url, params=hasil)

if response.status_code == 200: 
    data = response.json() 
    users = data['results']  
    sorted_users = sorted(users, key=lambda user: user['dob']['age'])
    for i, user in enumerate(sorted_users):
        gender = user['gender']
        first = user['name']['first']
        last = user['name']['last']
        title = user['name']['title']
        age = user['dob']['age']
        country = user['location']['country']

        print('     ')
        print(f'Pengguna {i + 1}')
        print(f'Nama : {first} {last}')
        print(f'Umur : {age}')
        print(f'Asal : {country}')
        
        if gender == 'male':
            print('Jenis Kelamin : Laki-laki')
        else:
            print('Jenis Kelamin : Perempuan')
        
else:
    print(f'Gagal mengambil data: {response.status_code}')
