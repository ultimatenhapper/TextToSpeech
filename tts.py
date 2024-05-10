from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = '/home/javi/projects/TextToSpeech/.env/lib/python3.11/site-packages/TTS/.models.json'
model_manager = ModelManager(path)
model_path, config_path, model_item = model_manager.download_model('tts_models/en/ljspeech/tacotron2-DDC')

synthesizer = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,

)

text = """This quote comes from the pre-Socratic philosopher Heraclitus, known for his cryptic sayings. Here's a breakdown of the meaning and context:

Meaning:

Evenminded: This refers to a balanced and impartial state of mind. It's about not being swayed by emotions or extremes.
Greatest virtue: Heraclitus considers even-mindedness the most important quality a person can possess.
Context:

Limited knowledge: We only have fragments of Heraclitus' work remaining. It's difficult to say for sure what he meant by "evenminded" in the grand scheme of his philosophy.
Possible interpretations:
It could be about approaching situations rationally and objectively.
It might connect to Heraclitus' ideas about balance and harmony in the universe. Even-mindedness reflects inner peace that aligns with the natural order.
Overall:

Even though the exact meaning is debated, the quote emphasizes the importance of a balanced and thoughtful approach to life. It's a concept that resonates across many philosophical traditions."""

output = synthesizer.tts(text)
synthesizer.save_wav(output, "audio.wav")