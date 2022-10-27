from rolepermissions.roles import AbastractUserRole

class Gerente(AbastractUserRole):
    avaible_permissions = {
        'cadastrar_produto':True,
        'liberar_desconto': True,
        'cadastrar_vendedor':True,
    }
    
class Vendedor(AbastractUserRole):
    avaible_permissions = {
        'realizar_venda': True
    }