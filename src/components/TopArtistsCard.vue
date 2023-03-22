<template>
  <div>
    <div class="m-4">
      <h3 style="color: black">Top Artists</h3>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for="(artist, index) in itemsToShow" class="col">
          <div class="card-block-round text-center">
            <a :href="artist.external_urls.spotify" target="_blank">
              <img class="card-img-top" :src="artist.images[0].url" :alt="artist.name"
                style="height: 280px; width: 280px; object-fit: cover; border-radius: 50%;">
            </a>
          </div>
          <div class="text-center">
            <h4 class="title mt-3">{{ artist.name.length > 16 ? artist.name.substr(0, 16) + '...' : artist.name }}</h4>
          </div>
        </div>
        <div class="col d-flex align-items-center" v-if="itemsToShow.length < result.items.length">
          <div class="card-block text-center justify-content-center">
            <button class="btn btn-outline-secondary" @click="showMore"
              style="font-size: 1.2em; padding: 10px 20px; font-weight: 800; display: flex; justify-content: center; align-items: center;">
              View More
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      result: {
        "items": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1aLfVgwt8eBrpvHcutWmqe"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "a cappella",
              "college a cappella"
            ],
            "href": "https://api.spotify.com/v1/artists/1aLfVgwt8eBrpvHcutWmqe",
            "id": "1aLfVgwt8eBrpvHcutWmqe",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb8c4a9d4a5f8004ad4d0195aa",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab676161000051748c4a9d4a5f8004ad4d0195aa",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f1788c4a9d4a5f8004ad4d0195aa",
                "width": 160
              }
            ],
            "name": "The Nor'easters",
            "popularity": 34,
            "type": "artist",
            "uri": "spotify:artist:1aLfVgwt8eBrpvHcutWmqe"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/41MozSoPIsD1dJM0CLPjZF"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "k-pop",
              "k-pop girl group"
            ],
            "href": "https://api.spotify.com/v1/artists/41MozSoPIsD1dJM0CLPjZF",
            "id": "41MozSoPIsD1dJM0CLPjZF",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5ebc9690bc711d04b3d4fd4b87c",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174c9690bc711d04b3d4fd4b87c",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178c9690bc711d04b3d4fd4b87c",
                "width": 160
              }
            ],
            "name": "BLACKPINK",
            "popularity": 87,
            "type": "artist",
            "uri": "spotify:artist:41MozSoPIsD1dJM0CLPjZF"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4Uc8Dsxct0oMqx0P6i60ea"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "bedroom pop",
              "pop"
            ],
            "href": "https://api.spotify.com/v1/artists/4Uc8Dsxct0oMqx0P6i60ea",
            "id": "4Uc8Dsxct0oMqx0P6i60ea",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5ebd3a1193ab04e0fb2b297e619",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174d3a1193ab04e0fb2b297e619",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178d3a1193ab04e0fb2b297e619",
                "width": 160
              }
            ],
            "name": "Conan Gray",
            "popularity": 82,
            "type": "artist",
            "uri": "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7nzSoJISlVJsn7O0yTeMOB"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "anime",
              "anime score",
              "japanese classical",
              "japanese soundtrack",
              "orchestral soundtrack"
            ],
            "href": "https://api.spotify.com/v1/artists/7nzSoJISlVJsn7O0yTeMOB",
            "id": "7nzSoJISlVJsn7O0yTeMOB",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5ebd26d9be0e533942c3e73875b",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174d26d9be0e533942c3e73875b",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178d26d9be0e533942c3e73875b",
                "width": 160
              }
            ],
            "name": "Joe Hisaishi",
            "popularity": 70,
            "type": "artist",
            "uri": "spotify:artist:7nzSoJISlVJsn7O0yTeMOB"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "pop"
            ],
            "href": "https://api.spotify.com/v1/artists/06HL4z0CvFAxyc27GXpf02",
            "id": "06HL4z0CvFAxyc27GXpf02",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb5a00969a4698c3132a15fbb0",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab676161000051745a00969a4698c3132a15fbb0",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f1785a00969a4698c3132a15fbb0",
                "width": 160
              }
            ],
            "name": "Taylor Swift",
            "popularity": 100,
            "type": "artist",
            "uri": "spotify:artist:06HL4z0CvFAxyc27GXpf02"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/52zMTJCKluDlFwMQWmccY7"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "k-pop",
              "k-pop girl group"
            ],
            "href": "https://api.spotify.com/v1/artists/52zMTJCKluDlFwMQWmccY7",
            "id": "52zMTJCKluDlFwMQWmccY7",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb80584436e5726afb70cee7f8",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab6761610000517480584436e5726afb70cee7f8",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f17880584436e5726afb70cee7f8",
                "width": 160
              }
            ],
            "name": "LOONA",
            "popularity": 64,
            "type": "artist",
            "uri": "spotify:artist:52zMTJCKluDlFwMQWmccY7"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6KImCVD70vtIoJWnq6nGn3"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "pop"
            ],
            "href": "https://api.spotify.com/v1/artists/6KImCVD70vtIoJWnq6nGn3",
            "id": "6KImCVD70vtIoJWnq6nGn3",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5ebf7db7c8ede90a019c54590bb",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174f7db7c8ede90a019c54590bb",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178f7db7c8ede90a019c54590bb",
                "width": 160
              }
            ],
            "name": "Harry Styles",
            "popularity": 91,
            "type": "artist",
            "uri": "spotify:artist:6KImCVD70vtIoJWnq6nGn3"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/2AfmfGFbe0A0WsTYm0SDTx"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "k-pop",
              "k-pop girl group"
            ],
            "href": "https://api.spotify.com/v1/artists/2AfmfGFbe0A0WsTYm0SDTx",
            "id": "2AfmfGFbe0A0WsTYm0SDTx",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb196f5af772aeb1bdd3a6be65",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174196f5af772aeb1bdd3a6be65",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178196f5af772aeb1bdd3a6be65",
                "width": 160
              }
            ],
            "name": "(G)I-DLE",
            "popularity": 76,
            "type": "artist",
            "uri": "spotify:artist:2AfmfGFbe0A0WsTYm0SDTx"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1z4g3DjTBBZKhvAroFlhOM"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "k-pop",
              "k-pop girl group"
            ],
            "href": "https://api.spotify.com/v1/artists/1z4g3DjTBBZKhvAroFlhOM",
            "id": "1z4g3DjTBBZKhvAroFlhOM",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb5bf330a57b9dcffd8f7b2c14",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab676161000051745bf330a57b9dcffd8f7b2c14",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f1785bf330a57b9dcffd8f7b2c14",
                "width": 160
              }
            ],
            "name": "Red Velvet",
            "popularity": 75,
            "type": "artist",
            "uri": "spotify:artist:1z4g3DjTBBZKhvAroFlhOM"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5fa13NJjmn2uQ3dxZDi2Ge"
            },
            "followers": {
              "href": null,
              "total": 0
            },
            "genres": [
              "v-pop"
            ],
            "href": "https://api.spotify.com/v1/artists/5fa13NJjmn2uQ3dxZDi2Ge",
            "id": "5fa13NJjmn2uQ3dxZDi2Ge",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb2de300e8eb56aac83abfdb4f",
                "width": 640
              },
              {
                "height": 320,
                "url": "https://i.scdn.co/image/ab676161000051742de300e8eb56aac83abfdb4f",
                "width": 320
              },
              {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f1782de300e8eb56aac83abfdb4f",
                "width": 160
              }
            ],
            "name": "Bich Phuong",
            "popularity": 48,
            "type": "artist",
            "uri": "spotify:artist:5fa13NJjmn2uQ3dxZDi2Ge"
          }
        ],
        "total": 50,
        "limit": 10,
        "offset": 0,
        "href": "https://api.spotify.com/v1/me/top/artists?limit=10&offset=0&time_range=long_term",
        "next": "https://api.spotify.com/v1/me/top/artists?limit=10&offset=10&time_range=long_term",
        "previous": null
      },
      itemsToShow: []
    }
  },
  mounted() {
    this.showMore()
  },
  methods: {
    showMore() {
      const startIndex = this.itemsToShow.length
      const endIndex = Math.min(startIndex + 5, this.result.items.length)
      this.itemsToShow.push(...this.result.items.slice(startIndex, endIndex))
    }
  }
}
</script>