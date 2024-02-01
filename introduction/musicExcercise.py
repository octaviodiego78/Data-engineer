from dataclasses import dataclass
from typing import List


@dataclass
class Song():

   length: float 
   title: str
   artist: "Artist"
   release: "Release"
   path: str
   genre: str
   created: str
   composer: str

@dataclass
class Artist():
   name: str 
   country: str 
   followers: List[str]
   birthdate: str

@dataclass
class Release():
   name: str
   coverPath: str
   songs: List[Song]
   author: Artist



