from phon.vphom import vphome
from text.cleaners import vietnamese_cleaners
# cov = vphome(nosuper=False,glottal=True)
# print(cov.phonemize('vì thấy nói toàn những Cléopâtre, Orion, Reine Margot, Pacifique, Limier vân vân.'))
print(vietnamese_cleaners('vì thấy nói toàn những Cléopâtre, Orion, Reine Margot, Pacifique, Limier vân vân.'))