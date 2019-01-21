import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'rd-frontend';
  loading = false;
  results = [];
  constructor(private api: ApiService) { }

  search(text: string) {
    this.loading = true;
    this.api.getResults(text).subscribe(resp => {
      console.log(resp);
      this.results = resp.message.prediction;
      this.loading = false;
      });
  }
}
