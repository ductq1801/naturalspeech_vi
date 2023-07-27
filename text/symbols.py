""" from https://github.com/keithito/tacotron """

"""
Defines the set of symbols used in text input to the model.
"""
_pad = "_"
_punctuation = ';:,.!?¡¿—…"«»“” '
#_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼ¹²³⁴⁵⁶⁷⁸ᴬᴮᶜᴰˀʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
_letters = 'AÁÀẠẢÃĂẰẮẶẲẴÂẤẦẬẨẪBCDĐEÉÈẺẼẸÊẾỀỂỄỆFGHIÍÌỊỈĨJKLMNOÓÒỌỎÕƠỚỜỢỠỞÔỐỒỘỖỔPQRSTUÚÙỤỦŨƯỨỪỰỮỬVWXYZaáàạảãăắằặẳẵâấầậẩẫbcdđeéèẻẽẹêếềểễệfghiíìịỉĩjklmnoóòọỏõơớờợỡởôốồộỗổpqrstuúùụủũưứừựữửvwxyz'

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")
#print('ɲ' in symbols)