import flet as ft

def main(page: ft.Page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    def calcular(e):
        if idade.value== '' or peso.value== str or '' or altura.value== str or '' or genero.value=='':
            page.banner.open = True
            page.update()
        else:
            valor_idade = float(idade.value)
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)

            # calcular valor de Tava de metabolismo basal
            tmb = 66 + (13.8 * valor_peso) + (5 * valor_altura) - (6.8 * valor_idade)
            tmb = float(f'{tmb: 2f}')

            #Exibir valor do TMB
            TMB.value = f'Your BMR is {tmb}'
            img_resultado.src = f'1.png'

            if genero.value == 'Woman':
                tmb = 665 + (9.6 * valor_peso) + (1.8 * valor_altura) - (4.7 * valor_idade)
                tmb = float(f'{tmb: 2f}')

                TMB.value = f'Your BMR is... {tmb}'
                
                img_resultado.src = f'1.png'
                detalhes.value = ' dont worry'

        #Lipar campos
        idade.value = ''
        peso.value = ''
        altura.value = ''
        genero.value = ''

        # Atualizar a pagina
        page.update()



    #configurando pagina

    page.appbar = ft.AppBar(
        leading = ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width = 40,
        title = ft.Text('Calculator BMR'),
        center_title = False,
        bgcolor = ft.colors.SURFACE_VARIANT

    )

    page.window_width = 400
    page.window_height = 600

    #config do banner de notificacao
    page.banner = ft.Banner(
        bgcolor = ft.colors.AMBER_100,
        leading = ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content = ft.Text('Oops, fill in all the fields'),
        actions = [
            ft.TextButton('OK', on_click = close_banner),
        ],
    )

    idade = ft.TextField(label='Age', hint_text= 'enter your age')
    altura = ft.TextField(label='Height', hint_text= 'enter your height')
    peso = ft.TextField(label='Weight', hint_text= 'enter your weight')
    genero = ft.Dropdown(
        label = 'Gender',
        hint_text = 'What is your Gender?',
        options=[
            ft.dropdown.Option('Man'),
            ft.dropdown.Option('Woman'),

        ]
    )

    b_calcular = ft.ElevatedButton(text='Calculate BMR', on_click=calcular)

    #Exibir o TMB e Resultado
    TMB = ft.Text('Your BMR is ...', size=30)
    detalhes = ft.Text('Enter your details', size=20)

    img_capa = ft.Image(
        src=f'icon.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info_app_resultado = ft.Column(
        controls=[
            TMB,
            detalhes,
        ]
    )

    img_resultado = ft.Image(
        src=f'iconf.png',
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    info = ft.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ]
    )
    
    #Layout da pagina

    layout = ft.ResponsiveRow(
        [
            ft.Container(
            info,
            padding = 5,
            col = {'sm':4, 'md':4, 'xl':4},
            alignment = ft.alignment.center,
        ),

         ft.Container(
            idade,
            padding = 5,
            #bgcolor = ft.colors.BLACK,
            col = {'sm':12, 'md':3, 'xl':3},
        ),

        ft.Container(
            altura,
            padding = 5,
            #bgcolor = ft.colors.BLACK,
            col = {'sm':12, 'md':3, 'xl':3},
        ),

         ft.Container(
             peso,
            padding = 5,
            #bgcolor = ft.colors.BLACK,
            col = {'sm':12, 'md':3, 'xl':3},
        ),

         ft.Container(
            genero,
            padding = 5,
            #bgcolor = ft.colors.WHITE,
            col = {'sm':12, 'md':3, 'xl':3},
        ),

         ft.Container(
            b_calcular,
            padding = 5,
            #bgcolor = ft.colors.WHITE,
            col = {'sm':12, 'md':3, 'xl':3},
        ),

        ]
    )

    page.add(layout)
ft.app(target=main)