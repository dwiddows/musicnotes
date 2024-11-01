
\version "2.24.0"

\paper {
  #(set-paper-size "custom")
  paper-width = 30\mm  % Set the desired paper width
  paper-height = 20\mm  % Set the desired paper height
  indent = 0\mm  % No indentation
  top-margin = 0\mm  % Remove top margin
  bottom-margin = 0\mm  % Remove bottom margin
  left-margin = 2\mm  % Set left margin
  right-margin = 2\mm  % Set right margin
}

\layout {
  \context {
    \Score
    \omit BarNumber
  }
}

% Disable the LilyPond tagline
\header {
  tagline = ##f  % This removes the tagline from the output
}

\fixed c, {  % Set absolute pitch for the chord
  \omit Staff.TimeSignature  % Hide the time signature
  \clef bass
  \chordmode {
    c1
  }
}
