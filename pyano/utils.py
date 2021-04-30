# -*- coding: utf-8 -*-
from mingus.containers import Note, NoteContainer, Bar, Track
from typing import List


class PianoUtils(object):
    """Generic class to hold general utility methods"""

    @staticmethod
    def note_to_string(note: Note) -> str:
        """Convert a mingus.containers.Note to a note string"""
        return "{0}-{1}".format(note.name, note.octave)

    @staticmethod
    def note_container_to_note_string_list(note_container: NoteContainer) -> List[str]:
        """Convert a mingus.containers.NoteContainer to a list of note strings"""
        return [PianoUtils.note_to_string(note) for note in note_container.notes]

    @staticmethod
    def bar_to_note_string_list(bar: Bar) -> List[str]:
        """Convert a mingus.containers.Bar to a list of note strings"""
        final_note_list = []
        for note_list in bar.bar:
            for note in note_list[-1]:
                final_note_list.append(PianoUtils.note_to_string(note))

        return final_note_list

    @staticmethod
    def track_to_note_string_list(track: Track) -> List[str]:
        """Convert a mingus.containers.Track to a list of note strings"""
        final_note_list = []
        for element in track.get_notes():
            for note in element[-1]:
                final_note_list.append(PianoUtils.note_to_string(note))

        return final_note_list
