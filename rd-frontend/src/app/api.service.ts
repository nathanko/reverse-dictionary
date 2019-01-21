import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import * as config from './app.config';
import { Observable } from 'rxjs';
import { ApiResponse } from './models/response.model';

@Injectable({ providedIn: 'root' })
export class ApiService {

  constructor(private http: HttpClient) {}

  getResults(text: string): Observable<ApiResponse> {
    const params = new HttpParams().set('text', text);
    return this.http.get<ApiResponse>(config.apiUrls.lookup, { params: params });
  }
}
