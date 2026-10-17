#!/usr/bin/env python3
"""Genera arima-aldizkaria.html (plantilla de correo para Brevo).

Uso:  python3 build.py
Lee imagenes.json (URLs de las imagenes subidas a Brevo) y escribe arima-aldizkaria.html.
Si falta alguna URL, usa una imagen de relleno para poder previsualizar.
"""
import html, json, os
here = os.path.dirname(os.path.abspath(__file__))
try:
    IMG = json.load(open(os.path.join(here, 'imagenes.json'), encoding='utf-8'))
except FileNotFoundError:
    IMG = {}
def img(key, w, h, label):
    return IMG.get(key) or f'https://placehold.co/{w}x{h}/e5f4fc/009de0?text={label}'
e = html.escape
CY, DEEP, TINT, INK, MUTE = '#009de0', '#00314a', '#e5f4fc', '#0b0f12', '#5a6770'
SANS = "Abel,'Arial Narrow',Arial,sans-serif"
SERIF = "'Cormorant Garamond',Georgia,'Times New Roman',serif"

A = [
 ('Urriak 2', 'Ortuella', 'Euskaraokea Gorbeia aretoan', 'Ortuellako Udala', 'Ortuellako DBHko gazteek euskaraz kantatzeko eguna izan zuten Gorbeia aretoan. Euskaraokea bi orduz musika, barre eta lotsarik gabeko mikrofonoa izan zen. Gazteek euskaraz gozatzeko modurik hoberena aurkitu zuten: kantatuz! Ortuellako Udalari eskerrik asko konfiantzagatik.'),
 ('Urriak 2', 'Sestao', 'Euskal Jaia: Zorroak tailerra', 'Gazte Sestao', 'Gaztegune Sestaoko haurrek Euskal Jaiaren giroa bizi izan zuten arratsaldean zehar, zorroak egiten eta apaintzen. Sormena eta ilusioa nagusi izan ziren tailer osoan, eta bakoitzak bere zorro berezia eraman zuen etxera. Eskerrik asko Gazte Sestaori!'),
 ('Urriak 3', 'Ugao-Miraballes', 'Herensugearen begia', 'Ugao-Miraballesko Udala', 'Familiek herensugearen begia egin zuten brotxeen tailerrean, bi saiotan. Gurasoak eta haurrak elkarrekin aritu ziren lanean, eta emaitza zoragarriak sortu ziren: brotxe bakoitza bakarra eta magikoa. Ugao-Miraballesko Udalari mila esker!'),
 ('Urriak 3', 'Irun', 'Decoupage tailerra', 'Irungo Udala', 'Irungo gazteek decoupage teknikarekin objektu arruntak artelan bihurtu zituzten. Arratsaldeko tailer lasai eta sortzaile bat izan zen, eta gazteen irudimenak harritu gintuen berriro. Eskerrik asko Irungo Udalari eta parte-hartzaile guztiei!'),
 ('Urriak 7', 'Portugalete', 'Portu Zorro Kustomizatuak', 'Portugaleteko Udala · Euskaraz Gozatuz', 'Santa Clara Kultur Etxean, 4 eta 7 urte arteko txikiek beren zorroak pertsonalizatu zituzten kolore eta marrazkiz. Euskaraz Gozatuz egitasmoaren barruan, jolasa eta hizkuntza batera ibili ziren. Portugaleteko Udalari eskerrik asko!'),
 ('Urriak 10', 'Erandio', 'Gau Beltza: kriseiluak', 'TAUPA Erandio', 'Erandioko familiek Gau Beltzaren giroan kriseiluak sortu zituzten, bi saiotan. Argia, ilusioa eta barre asko izan ziren tailerrean. TAUPAri eskerrik asko gu gogoratzeagatik!'),
 ('Urriak 16', 'Portugalete', 'Soja kandela trampantojoak', 'Portugaleteko Udala · Euskaraz Gozatuz', '8 eta 12 urte arteko gaztetxoek soja argizariarekin trampantojo kandelak egin zituzten, itxura harrigarriko emaitzekin. Euskaraz Gozatuz programaren beste saio gozagarri bat Santa Clara Kultur Etxean. Eskerrik asko Portugaleteko Udalari!'),
 ('Urriak 2–16', 'Inguru Minguru', 'Sormena, berrerabilpena eta komunitatea', 'Ekogune · Arima', 'Hilabete osoan Inguru Minguru tailerrek bizirik jarraitu dute: ostiral arratsaldeko saioak (urriaren 2an, 9an eta 16an) eta Ekogunerekin elkarlanean helduentzako ikastaroak, hala nola etxeko konponketa txikiak, hegazti-etxeak eta ehungailuak. Eskuak lanean, ideiak bueltaka eta ikasteko gogo handia.'),
]

rows = ''
for i, (d, place, t, c, txt) in enumerate(A):
    bg = TINT if i % 2 else '#ffffff'
    rows += f'''
<tr><td style="background:{bg};padding:0;border-bottom:1px solid #c9d2d7">
  <img src="{img(f'foto{i+1}', 600, 400, 'Argazkia+' + str(i+1))}" width="600" alt="{e(t)}" style="display:block;width:100%;max-width:600px;height:auto;border:0">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td class="pad" style="padding:28px 36px 36px">
    <div style="font-family:{SERIF};font-size:52px;line-height:46px;font-weight:300;color:{CY}">{i+1:02d}</div>
    <div style="font-family:{SANS};font-size:11px;letter-spacing:3px;text-transform:uppercase;color:{INK};margin:10px 0 8px"><span style="color:{CY}">{e(d)}</span> &nbsp;&mdash;&nbsp; {e(place)}</div>
    <div style="font-family:{SERIF};font-size:30px;line-height:31px;font-weight:500;color:{INK}">{e(t)}</div>
    <div style="font-family:{SERIF};font-style:italic;font-size:18px;color:{MUTE};margin:6px 0 12px">{e(c)}</div>
    <div style="font-family:{SANS};font-size:17px;line-height:25px;color:{INK}">{e(txt)}</div>
  </td></tr></table>
</td></tr>'''

out = f'''<!doctype html>
<html lang="eu"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Arima aldizkaria · 2026ko urria</title>
<link href="https://fonts.googleapis.com/css2?family=Abel&family=Cormorant+Garamond:ital,wght@0,300;0,500;1,300;1,500&display=swap" rel="stylesheet">
<style>
  body{{margin:0;padding:0;background:#e9eef1}}
  @media (max-width:620px){{
    .wrap{{width:100%!important}} .pad{{padding-left:22px!important;padding-right:22px!important}}
    .h1{{font-size:46px!important;line-height:46px!important}} .side{{display:block!important;width:100%!important}}
  }}
</style></head>
<body style="margin:0;padding:0;background:#e9eef1">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">Azken hamabost egunetako tailerrak: kolorea, sormena eta euskara.</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#e9eef1"><tr><td align="center" style="padding:20px 0">
<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" style="width:600px;max-width:600px;background:#ffffff">

<tr><td style="padding:10px 36px;font-family:{SANS};font-size:11px;color:{MUTE};text-align:center" class="pad">Mezua ondo ikusten ez baduzu, <a href="{{{{ mirror }}}}" style="color:{CY}">ireki nabigatzailean</a></td></tr>

<tr><td class="pad" style="padding:20px 36px 14px;border-bottom:2px solid {INK}">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
    <td align="left"><img src="{img('logo', 360, 115, 'ARIMA')}" height="38" alt="Arima" style="display:block;height:38px;width:auto;border:0"></td>
    <td align="right" style="font-family:{SANS};font-size:11px;letter-spacing:3px;text-transform:uppercase;color:{INK}">Aldizkaria &middot; N&ordm; 01<br>2026ko urria</td>
  </tr></table>
</td></tr>

<tr><td style="border-bottom:2px solid {INK}">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>
    <td class="pad side" style="padding:44px 24px 38px 36px;vertical-align:top">
      <div class="h1" style="font-family:{SERIF};font-size:62px;line-height:58px;font-weight:300;letter-spacing:-1px;color:{INK}">Esku <i style="color:{CY};font-weight:500">lanetik</i> bihotzera</div>
      <div style="font-family:{SERIF};font-style:italic;font-size:21px;line-height:28px;color:{INK};margin-top:18px">Azken hamabost egunetako tailerrak: kolorea, sormena eta euskara Bizkaiko txoko askotan.</div>
    </td>
    <td class="side" width="140" style="background:{CY};padding:22px 18px;vertical-align:top;color:#ffffff">
      <div style="font-family:{SERIF};font-size:70px;line-height:62px;font-weight:300">08</div>
      <div style="font-family:{SANS};font-size:10px;letter-spacing:2px;text-transform:uppercase;margin-top:70px;line-height:16px">Tailer eta ikastaro<br>Urriak 2&ndash;16</div>
    </td>
  </tr></table>
</td></tr>

<tr><td class="pad" style="padding:40px 36px;border-bottom:2px solid {INK};font-family:{SANS};font-size:18px;line-height:27px;color:{INK}">
  <div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;color:{CY};border-top:3px solid {CY};padding-top:8px;width:120px;margin-bottom:16px">Editoriala</div>
  Urria ez da geldirik egon! Azken hamabost egunetan, Arima-k tailerrez, jolasez eta sormenez bete ditu gazteleku, kultur etxe eta aretoak. Haurrak, gazteak, familiak eta helduak: guztiek utzi digute zerbait ederra gure eskuetan.<br><br>
  Eskerrik asko gu kontratatu gaituzuen udalei eta elkarteei, eta batez ere parte hartu duten guztiei. Zuek egiten duzue posible!
</td></tr>
{rows}

<tr><td class="pad" style="background:{DEEP};padding:56px 36px;color:#ffffff">
  <div class="h1" style="font-family:{SERIF};font-size:42px;line-height:41px;font-weight:300">Zure herrian <i style="color:{CY};font-weight:500">tailer</i> bat nahi duzu?</div>
  <div style="font-family:{SANS};font-size:18px;line-height:27px;margin:16px 0 22px">Udalak, gaztelekuak, elkarteak, ikastetxeak eta familiak: tailerrak zuen neurrira prestatzen ditugu. Idatzi iezaguzu eta elkarrekin zerbait polita antolatuko dugu!</div>
  <a href="mailto:arimacooltour@gmail.com" style="display:inline-block;background:{CY};color:#ffffff;text-decoration:none;padding:14px 24px;font-family:{SANS};font-size:15px;letter-spacing:2px">arimacooltour@gmail.com</a>
</td></tr>

<tr><td class="pad" style="padding:20px 36px;font-family:{SANS};font-size:11px;line-height:17px;letter-spacing:1px;color:{MUTE};text-align:center">
  Arima &middot; Euskaraz, eskuz, bihotzez<br>
  Mezu hau jaso nahi ez baduzu, <a href="{{{{ unsubscribe }}}}" style="color:{CY}">kendu zaitez zerrendatik hemen</a>.
</td></tr>

</table></td></tr></table>
</body></html>
'''
open(os.path.join(here, 'arima-aldizkaria.html'), 'w', encoding='utf-8').write(out)
print('OK', len(out), 'bytes')
