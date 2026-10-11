import kagglehub

# Download latest version
path = kagglehub.dataset_download(
    "radcliffe/3-million-sudoku-puzzles-with-ratings",
    output_dir="data/",
)
