
\version "2.24.0"

\paper {
  #(set-paper-size "custom")
  paper-width = 30\mm
  paper-height = 20\mm
  indent = 0\mm
  top-margin = 0\mm
  bottom-margin = 0\mm
  left-margin = 2\mm
  right-margin = 2\mm
}

\layout {
  \context {
    \Score
    \omit BarNumber
  }
}

\header {
  tagline = ##f
}

\fixed c {
  \omit Staff.TimeSignature
  \clef treble
  \chordmode {
    c1:m
  }
}
