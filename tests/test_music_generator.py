import unittest
from openmuse.music_generator import MusicGenerator
from music21 import stream

class TestMusicGenerator(unittest.TestCase):

    def setUp(self):
        self.music_generator = MusicGenerator()

    def test_generate_music(self):
        music = self.music_generator.generate_music()
        self.assertIsInstance(music, stream.Stream)
        self.assertGreater(len(music), 0)

    def test_save_music(self):
        music = self.music_generator.generate_music()
        file_path = 'test_output.mid'
        self.music_generator.save_music(music, file_path)
        with open(file_path, 'rb') as f:
            content = f.read()
        self.assertGreater(len(content), 0)

if __name__ == '__main__':
    unittest.main()
