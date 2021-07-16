import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {DeezerRequestService} from '../../services/deezer-request.service';

@Component({
  selector: 'app-artist',
  templateUrl: './artist.component.html',
  styleUrls: ['./artist.component.scss']
})
export class ArtistComponent implements OnInit {
  artist: any;
  topTracks: any;
  artistRelated: any[];
  loading = true;

  constructor(
    private activatedRoute: ActivatedRoute,
    private deezerRequest: DeezerRequestService) {
  }

  ngOnInit(): void {
    this.initRouteParam();
  }

  initRouteParam() {
    this.activatedRoute.params
      .subscribe(params => {
        this.deezerRequest.getArtist(params.id)
          .subscribe(artist => {
            this.artist = artist;
            this.initTopTracks();
            this.initArtistRelated();
          }).add(() => this.loading = false);
      });
  }

  initTopTracks() {
    this.deezerRequest.getArtistTopTrack(this.artist.id)
      .subscribe((topTracks: any) => {
        this.topTracks = topTracks.data;
      });
  }

  initArtistRelated() {
    this.deezerRequest.getArtistRelated(this.artist.id)
        .subscribe((artists: any) => {
          this.artistRelated = artists.data;
        });
  }
}
