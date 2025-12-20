from pyfrontkit import CreateFont, HeaderFont,nav, t, CreateColor, div, main, img, header, footer, HtmlDoc, a, button,hr

doc=HtmlDoc(title="example1",
    links=["https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap",
           "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"]
            )
header(id="top").form(background="#252220",height="116px",color="white").align("row",padding="20px", gap="350px")

top(div(id="left").form(height="100px",width="258px").align("column",padding="20px").margin(left="80px", bottom="35px"),
    div(id="right").align("row","10px"))  


right(
    div(id="second").form(height="80px",width="290px").align("row","20px","20px"),
    div(id="third").form(height="80px",width="320px").align("row","20px","20px"))
     
left(img(src="imagen/logo.png",height="78px",width="208px"))

second(div(id="green_back1").form("64px","64px",background="linear-gradient(90deg, #196730, #439a0d)",border_radius="5px"),
       div(ctn_p="Have any question?",ctn_h2="1(225) 5556234)").align("column","5px","10px",fsize="14px")) 
third(div(id="green_back2").form("64px","64px",background="linear-gradient(90deg, #196730, #439a0d)",border_radius="5px"),
      div(ctn_p="Our address",ctn_h2="3445 Queen Steet,PA").align("column","5px","10px",fsize="14px"))

green_back1(img(src="imagen/phone.png",height="60px",width="60px"))
green_back2(img(src="imagen/location.png",height="60px",width="60px"))

div(id="nbarra").position(top="128px", left="116px",).form(height='63px', width="1300px", background ="#F5F5F0", border_radius="7px").align("row","280px")

nbarra(nav(id="bar_left").align("row","10px","10px" ),
      div(id="bar_right").align("row","10px","10px" ).form(width="400px"))

bar_left(a(ctn_span="Home").form(background="linear-gradient(90deg, #196730, #439a0d)",color="white",border_radius="8px",height='20px',width="44px").align("row",padding="12px",fsize="16px"),
         a(ctn_none="Gardening", class_="barra").form(border_radius="8px",height="20px").hover("white","linear-gradient(90deg, #196730, #439a0d)").align("row",padding="12px",fsize="16px"),
         a(ctn_none="Services", class_="barra"),
         a(ctn_none="Projects",class_="barra"),
         a(ctn_none="Blog",class_="barra"),
         a(ctn_none="Shop",class_="barra"),
         a(ctn_none="Pages",class_="barra"))
bar_right( a(ctn_i=("","fab fa-facebook"),class_="rrss").align("column",padding="7px",fsize="26px").form("40px","40px",border_radius="8px"),
           a(ctn_i=("","fab fa-x-twitter"),class_="rrss"),
           a(ctn_i=("","fab fa-skype"),class_="rrss"),
           a(ctn_i=("","fab fa-instagram"),class_="rrss"),
           a(ctn_none="Get a Free Quote").hover(scale=1.2).form(background="linear-gradient(90deg, #196730, #439a0d)",color="white",border_radius="8px",height='20px',width="120px").align("row",padding="12px",fsize="16px") )


div(id="center").form(height='800px',background="url(imagen/slider3.jpg)")
center(div(ctn_strong="XTRA Gardening").position("absolute","400px","230px").form("180px","50px","10px","linear-gradient(90deg, #196730, #439a0d)","white").align("column",padding="13px",fsize="24px"),
       div(ctn_strong="The Best Fertilizer Is").position("absolute","450px","200px").form("550px","70px","10px","white","#084808").align("column",padding="15px",pad_left="30px",pad_right="30px",fsize="56px"),
       div(ctn_strong="A Gardener Is").position("absolute","540px","520px").form("210px","50px","10px","#252220","white").align("column",padding="8px",pad_left="14px",pad_right="14px",fsize="34px"),
       )


div(id="section").align("row",'20px',"20px","80px","80px")
section(div(id="card_0").form("300px","375px","5px","linear-gradient(90deg, #196730, #439a0d)","white").align("column","70px",pad_top="50px",text_align="center"),
        div(id="card_1").form("300px","375px","5px",color="green").align("column","40px",text_align="center",fsize="22px"),
        div(id="card_2").form("300px","375px","5px",color="green").align("column","40px",text_align="center",fsize="22px"),
        div(id="card_3").form("300px","375px","5px",color="green").align("column","40px",text_align="center",fsize="22px"))

card_0(div(ctn_strong="For All Your\n Gardening \nNeeds",ctn_span="____").align("column",fsize="28px"),
        div(ctn_p="Home Gardening \nSupplies and Gifts").align("column",fsize="18px"))

card_1(div(id="block_image").form("300px","300px").align("column","20px",pad_left="100px",pad_top="50px",fsize="24px"),
        t(ctn_strong="Gardening Services"),
       div(id="block_text",ctn_p="A beautiful garden can transform a\n property. Whether you're trying to \n recreate the gardens").form(color="grey").align("column","40px",fsize="16px")),
block_image(img(src="imagen/plant.png",height="100px",width="100px"))
block_text(a(ctn_strong ="Read More").hover(scale=1.2).form("100px","35px","5px", "linear-gradient(90deg, #196730, #439a0d)" ,"white").margin(left="100px").align("column",pad_top='11px',fsize="16px"))


card_2(div(id="block_image1").form("300px","300px").align("column","20px",pad_left="100px",pad_top="50px",fsize="24px"),
        t(ctn_strong="Plants Planting"),
       div(id="block_text1",ctn_p="Whether you choose to eat vegetarian \nor just want to eat a little healthier in  \n green house").form(color="grey").align("column","40px",fsize="16px")),
block_image1(img(src="imagen/seeds.png",height="100px",width="100px"))
block_text1(a(ctn_strong ="Read More").hover(scale=1.2).form("100px","35px","5px", "linear-gradient(90deg, #196730, #439a0d)" ,"white").margin(left="100px").align("column",pad_top='11px',fsize="16px"))


card_3(div(id="block_image2").form("300px","300px").align("column","20px",pad_left="100px",pad_top="50px",fsize="24px"),
        t(ctn_strong="Gardening Services"),
       div(id="block_text2",ctn_p="A beautiful garden can transform a\n property. Whether you're trying to \n recreate the gardens").form(color="grey").align("column","40px",fsize="16px")),

block_image2(img(src="imagen/digger.png",height="100px",width="100px"))
block_text2(a(ctn_strong ="Read More").hover(scale=1.2).form("100px","35px","5px", "linear-gradient(90deg, #196730, #439a0d)" ,"white").margin(left="100px").align("column",pad_top='11px',fsize="16px"))

           
div(id="back").position(top="756px")
back(img(src="imagen/back.png",height="200px",width='1600x'))


div(id="back2").position(top="1470px")
back2(img(src="imagen/fore.png",height="200px",width='1600x'))

footer(id="piedpagina").form(height="480px",background="black",color="grey").align("column","50px",pad_top="200px")
piedpagina(div(id="logo").margin("50px",left="662px"),
          div(ctn_p="Call Us: 001 (818) 23 33 456 \n 14 King Land Street, New York, USA").form(color="white").align("column","40px",fsize="22px",text_align="center").margin(left="5px"),
          a(ctn_none="Get a Free Quote").hover(scale=1.2).form(background="linear-gradient(90deg, #196730, #439a0d)",color="white",border_radius="8px",height='20px',width="120px").align("row",padding="12px",fsize="16px").margin(left="695px"),
          hr(style="border: none; height: 2px; width: 100%; margin: 2px 0;"),          
          div(ctn_p="© Copyright 2025. All Right Reserved.Inspired in a Wordpress theme. Proudly maked with Pyfrontkit").form(color="grey"))

logo(img(src="imagen/logo.png",height="78px",width="208px"))












doc.create_document()
CreateFont("Roboto")
