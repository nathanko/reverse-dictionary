export interface ApiResponse {
  'message': {
    'prediction': {
      'cosine': number
      'definition': string,
      'entry': string,
    }[]
  };
}
