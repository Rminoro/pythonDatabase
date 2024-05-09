import firebase_admin
from firebase_admin import credentials, firestore

# Inicialize o SDK do Firebase com suas credenciais
cred = credentials.Certificate('./challengemobile-2a2e2-firebase-adminsdk-69efh-f91d9ccb52.json')
firebase_admin.initialize_app(cred)

# Verifique se a conexão foi bem-sucedida
print("Conexão com o Firestore estabelecida com sucesso.")

# Acesse o Firestore
db = firestore.client()

# Crie uma nova coleção para usuários
usuarios_ref = db.collection('usuarios')

# Insira dados na coleção de usuários
usuario_data = {
    'id': 1,
    'cpf': '123.456.789-00',
    'senha': 'senha123'
}
usuarios_ref.document('usuario1').set(usuario_data)

# Agora, crie uma nova coleção para perfis
perfis_ref = db.collection('perfis')

# Insira dados na coleção de perfis
perfil_data = {
    'cargo': 'Analista',
    'estado': 'SP',
    'nome': 'Rafael Minoro'
}
perfis_ref.document('perfil1').set(perfil_data)

print("Dados inseridos com sucesso.")
