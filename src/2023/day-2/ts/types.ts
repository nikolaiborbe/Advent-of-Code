// -> [(id, [(blue, green, red)])]

export type gameScores = [number, number, number];
export type game = [number, gameScores[]];
export type Games = game[];