<template>
  <div>
    <div class="m-4">
      <h3 style="color: black">Top Songs</h3>
    </div>
    <div class="container-fluid">
      <div class="scrolling-wrapper row flex-row flex-nowrap mt-4 pt-2">
        <div v-for="(track, index) in itemsToShow" class="col">
          <div class="card-block">
            <a :href="track.external_urls.spotify" target="_blank">
              <img class="card-img-top" :src="track.album.images[0].url" :alt="track.album.name">
            </a>
          </div>
          <div>
            <h4 class="title mt-3">{{ track.name.length > 16 ? track.name.substr(0, 16) + '...' : track.name }}</h4>
            <h4 class="sub-title-1 mt-1">{{ track.artists[0].name }}</h4>
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
            "album": {
              "album_type": "ALBUM",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/7nzSoJISlVJsn7O0yTeMOB"
                  },
                  "href": "https://api.spotify.com/v1/artists/7nzSoJISlVJsn7O0yTeMOB",
                  "id": "7nzSoJISlVJsn7O0yTeMOB",
                  "name": "Joe Hisaishi",
                  "type": "artist",
                  "uri": "spotify:artist:7nzSoJISlVJsn7O0yTeMOB"
                }
              ],
              "available_markets": [
                "AD",
                "AE",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BH",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IN",
                "IS",
                "IT",
                "JO",
                "KW",
                "LB",
                "LI",
                "LT",
                "LU",
                "LV",
                "MA",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PH",
                "PL",
                "PS",
                "PT",
                "PY",
                "QA",
                "RO",
                "SA",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TN",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/2ZHxPDTCRU5STetdmXeW6p"
              },
              "href": "https://api.spotify.com/v1/albums/2ZHxPDTCRU5STetdmXeW6p",
              "id": "2ZHxPDTCRU5STetdmXeW6p",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b273b8ca4003c6774ffad9ee23e6",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e02b8ca4003c6774ffad9ee23e6",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d00004851b8ca4003c6774ffad9ee23e6",
                  "width": 64
                }
              ],
              "name": "Princess Mononoke Soundtrack",
              "release_date": "1997-07-02",
              "release_date_precision": "day",
              "total_tracks": 33,
              "type": "album",
              "uri": "spotify:album:2ZHxPDTCRU5STetdmXeW6p"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/7nzSoJISlVJsn7O0yTeMOB"
                },
                "href": "https://api.spotify.com/v1/artists/7nzSoJISlVJsn7O0yTeMOB",
                "id": "7nzSoJISlVJsn7O0yTeMOB",
                "name": "Joe Hisaishi",
                "type": "artist",
                "uri": "spotify:artist:7nzSoJISlVJsn7O0yTeMOB"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NO",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "disc_number": 1,
            "duration_ms": 128373,
            "explicit": false,
            "external_ids": {
              "isrc": "JPTK09780818"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/0KeqW4my39At2Ke1mVFYBF"
            },
            "href": "https://api.spotify.com/v1/tracks/0KeqW4my39At2Ke1mVFYBF",
            "id": "0KeqW4my39At2Ke1mVFYBF",
            "is_local": false,
            "name": "Princess Mononoke Theme Song",
            "popularity": 44,
            "preview_url": "https://p.scdn.co/mp3-preview/cd906c1f9760653a24bbdc2aa91fadaf262aeb62?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 18,
            "type": "track",
            "uri": "spotify:track:0KeqW4my39At2Ke1mVFYBF"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/5fa13NJjmn2uQ3dxZDi2Ge"
                  },
                  "href": "https://api.spotify.com/v1/artists/5fa13NJjmn2uQ3dxZDi2Ge",
                  "id": "5fa13NJjmn2uQ3dxZDi2Ge",
                  "name": "Bich Phuong",
                  "type": "artist",
                  "uri": "spotify:artist:5fa13NJjmn2uQ3dxZDi2Ge"
                }
              ],
              "available_markets": [],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/0JoA8Z6TWI31c6uWXldxyU"
              },
              "href": "https://api.spotify.com/v1/albums/0JoA8Z6TWI31c6uWXldxyU",
              "id": "0JoA8Z6TWI31c6uWXldxyU",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b2734ff4ae8820513dc663f1006a",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e024ff4ae8820513dc663f1006a",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d000048514ff4ae8820513dc663f1006a",
                  "width": 64
                }
              ],
              "name": "tâm trạng tan hơi chậm một chút",
              "release_date": "2018-03-01",
              "release_date_precision": "day",
              "total_tracks": 4,
              "type": "album",
              "uri": "spotify:album:0JoA8Z6TWI31c6uWXldxyU"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/5fa13NJjmn2uQ3dxZDi2Ge"
                },
                "href": "https://api.spotify.com/v1/artists/5fa13NJjmn2uQ3dxZDi2Ge",
                "id": "5fa13NJjmn2uQ3dxZDi2Ge",
                "name": "Bich Phuong",
                "type": "artist",
                "uri": "spotify:artist:5fa13NJjmn2uQ3dxZDi2Ge"
              }
            ],
            "available_markets": [],
            "disc_number": 1,
            "duration_ms": 208695,
            "explicit": false,
            "external_ids": {
              "isrc": "VNA0M1907691"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/2LKI0fGEKR3RWAiY2jqq8k"
            },
            "href": "https://api.spotify.com/v1/tracks/2LKI0fGEKR3RWAiY2jqq8k",
            "id": "2LKI0fGEKR3RWAiY2jqq8k",
            "is_local": false,
            "name": "Một Cú Lừa",
            "popularity": 0,
            "preview_url": null,
            "track_number": 2,
            "type": "track",
            "uri": "spotify:track:2LKI0fGEKR3RWAiY2jqq8k"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/4VbAtGhXMJr2AGXa8fkcRu"
                  },
                  "href": "https://api.spotify.com/v1/artists/4VbAtGhXMJr2AGXa8fkcRu",
                  "id": "4VbAtGhXMJr2AGXa8fkcRu",
                  "name": "I-LAND",
                  "type": "artist",
                  "uri": "spotify:artist:4VbAtGhXMJr2AGXa8fkcRu"
                }
              ],
              "available_markets": [],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/5sDl9lSChCR6f1CY8EsAsL"
              },
              "href": "https://api.spotify.com/v1/albums/5sDl9lSChCR6f1CY8EsAsL",
              "id": "5sDl9lSChCR6f1CY8EsAsL",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b2737be0fa7a6e19b0eeeb6c4407",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e027be0fa7a6e19b0eeeb6c4407",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d000048517be0fa7a6e19b0eeeb6c4407",
                  "width": 64
                }
              ],
              "name": "Into the I-Land",
              "release_date": "2020-06-26",
              "release_date_precision": "day",
              "total_tracks": 1,
              "type": "album",
              "uri": "spotify:album:5sDl9lSChCR6f1CY8EsAsL"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/4VbAtGhXMJr2AGXa8fkcRu"
                },
                "href": "https://api.spotify.com/v1/artists/4VbAtGhXMJr2AGXa8fkcRu",
                "id": "4VbAtGhXMJr2AGXa8fkcRu",
                "name": "I-LAND",
                "type": "artist",
                "uri": "spotify:artist:4VbAtGhXMJr2AGXa8fkcRu"
              }
            ],
            "available_markets": [],
            "disc_number": 1,
            "duration_ms": 217322,
            "explicit": false,
            "external_ids": {
              "isrc": "KRA492000740"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/0nTMrb8liUqXmEH9MZQqtV"
            },
            "href": "https://api.spotify.com/v1/tracks/0nTMrb8liUqXmEH9MZQqtV",
            "id": "0nTMrb8liUqXmEH9MZQqtV",
            "is_local": false,
            "name": "Into the I-LAND - Applicants Version",
            "popularity": 0,
            "preview_url": null,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:0nTMrb8liUqXmEH9MZQqtV"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/55fhWPvDiMpLnE4ZzNXZyW"
                  },
                  "href": "https://api.spotify.com/v1/artists/55fhWPvDiMpLnE4ZzNXZyW",
                  "id": "55fhWPvDiMpLnE4ZzNXZyW",
                  "name": "Noah Cyrus",
                  "type": "artist",
                  "uri": "spotify:artist:55fhWPvDiMpLnE4ZzNXZyW"
                }
              ],
              "available_markets": [
                "SK"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/71EPoeTo5QAlsr2OWCRNhM"
              },
              "href": "https://api.spotify.com/v1/albums/71EPoeTo5QAlsr2OWCRNhM",
              "id": "71EPoeTo5QAlsr2OWCRNhM",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b2737aa8305cc058141d02c5f4c3",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e027aa8305cc058141d02c5f4c3",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d000048517aa8305cc058141d02c5f4c3",
                  "width": 64
                }
              ],
              "name": "I Burned LA Down",
              "release_date": "2022-04-08",
              "release_date_precision": "day",
              "total_tracks": 1,
              "type": "album",
              "uri": "spotify:album:71EPoeTo5QAlsr2OWCRNhM"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/55fhWPvDiMpLnE4ZzNXZyW"
                },
                "href": "https://api.spotify.com/v1/artists/55fhWPvDiMpLnE4ZzNXZyW",
                "id": "55fhWPvDiMpLnE4ZzNXZyW",
                "name": "Noah Cyrus",
                "type": "artist",
                "uri": "spotify:artist:55fhWPvDiMpLnE4ZzNXZyW"
              }
            ],
            "available_markets": [
              "SK"
            ],
            "disc_number": 1,
            "duration_ms": 195252,
            "explicit": false,
            "external_ids": {
              "isrc": "USQX92105689"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/34Mg7rSCT7nRsf1kVCAvgz"
            },
            "href": "https://api.spotify.com/v1/tracks/34Mg7rSCT7nRsf1kVCAvgz",
            "id": "34Mg7rSCT7nRsf1kVCAvgz",
            "is_local": false,
            "name": "I Burned LA Down",
            "popularity": 13,
            "preview_url": "https://p.scdn.co/mp3-preview/8a288b1e6c4c259a195b280ae292b5feb58343da?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:34Mg7rSCT7nRsf1kVCAvgz"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/6RHTUrRF63xao58xh9FXYJ"
                  },
                  "href": "https://api.spotify.com/v1/artists/6RHTUrRF63xao58xh9FXYJ",
                  "id": "6RHTUrRF63xao58xh9FXYJ",
                  "name": "IVE",
                  "type": "artist",
                  "uri": "spotify:artist:6RHTUrRF63xao58xh9FXYJ"
                }
              ],
              "available_markets": [
                "AD",
                "AE",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BH",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IN",
                "IS",
                "IT",
                "JO",
                "JP",
                "KW",
                "LB",
                "LI",
                "LT",
                "LU",
                "LV",
                "MA",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PH",
                "PL",
                "PS",
                "PT",
                "PY",
                "QA",
                "RO",
                "SA",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TN",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/1AFVTHHm7kKoQ6Rgb25x3p"
              },
              "href": "https://api.spotify.com/v1/albums/1AFVTHHm7kKoQ6Rgb25x3p",
              "id": "1AFVTHHm7kKoQ6Rgb25x3p",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b2739016f58cc49e6473e1207093",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e029016f58cc49e6473e1207093",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d000048519016f58cc49e6473e1207093",
                  "width": 64
                }
              ],
              "name": "LOVE DIVE",
              "release_date": "2022-04-05",
              "release_date_precision": "day",
              "total_tracks": 2,
              "type": "album",
              "uri": "spotify:album:1AFVTHHm7kKoQ6Rgb25x3p"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/6RHTUrRF63xao58xh9FXYJ"
                },
                "href": "https://api.spotify.com/v1/artists/6RHTUrRF63xao58xh9FXYJ",
                "id": "6RHTUrRF63xao58xh9FXYJ",
                "name": "IVE",
                "type": "artist",
                "uri": "spotify:artist:6RHTUrRF63xao58xh9FXYJ"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "JP",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NO",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "disc_number": 1,
            "duration_ms": 177186,
            "explicit": false,
            "external_ids": {
              "isrc": "KRA382204375"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/0Q5VnK2DYzRyfqQRJuUtvi"
            },
            "href": "https://api.spotify.com/v1/tracks/0Q5VnK2DYzRyfqQRJuUtvi",
            "id": "0Q5VnK2DYzRyfqQRJuUtvi",
            "is_local": false,
            "name": "LOVE DIVE",
            "popularity": 80,
            "preview_url": "https://p.scdn.co/mp3-preview/ffeda0e70f8e10861d42135e1cee1c4ea949e09b?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:0Q5VnK2DYzRyfqQRJuUtvi"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/4Uc8Dsxct0oMqx0P6i60ea"
                  },
                  "href": "https://api.spotify.com/v1/artists/4Uc8Dsxct0oMqx0P6i60ea",
                  "id": "4Uc8Dsxct0oMqx0P6i60ea",
                  "name": "Conan Gray",
                  "type": "artist",
                  "uri": "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea"
                }
              ],
              "available_markets": [
                "AD",
                "AE",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BH",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IN",
                "IS",
                "IT",
                "JO",
                "JP",
                "KW",
                "LB",
                "LI",
                "LT",
                "LU",
                "LV",
                "MA",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PH",
                "PL",
                "PS",
                "PT",
                "PY",
                "QA",
                "RO",
                "SA",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TN",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/0DvIDMUOMaaVbXfDVt8jZS"
              },
              "href": "https://api.spotify.com/v1/albums/0DvIDMUOMaaVbXfDVt8jZS",
              "id": "0DvIDMUOMaaVbXfDVt8jZS",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b27361724ba7c381d7b067027a51",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e0261724ba7c381d7b067027a51",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d0000485161724ba7c381d7b067027a51",
                  "width": 64
                }
              ],
              "name": "Overdrive",
              "release_date": "2021-02-19",
              "release_date_precision": "day",
              "total_tracks": 1,
              "type": "album",
              "uri": "spotify:album:0DvIDMUOMaaVbXfDVt8jZS"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/4Uc8Dsxct0oMqx0P6i60ea"
                },
                "href": "https://api.spotify.com/v1/artists/4Uc8Dsxct0oMqx0P6i60ea",
                "id": "4Uc8Dsxct0oMqx0P6i60ea",
                "name": "Conan Gray",
                "type": "artist",
                "uri": "spotify:artist:4Uc8Dsxct0oMqx0P6i60ea"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "JP",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NO",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "disc_number": 1,
            "duration_ms": 183070,
            "explicit": true,
            "external_ids": {
              "isrc": "USUM72100677"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/3QyoC6OvQUmpQwQZ18iaTs"
            },
            "href": "https://api.spotify.com/v1/tracks/3QyoC6OvQUmpQwQZ18iaTs",
            "id": "3QyoC6OvQUmpQwQZ18iaTs",
            "is_local": false,
            "name": "Overdrive",
            "popularity": 66,
            "preview_url": "https://p.scdn.co/mp3-preview/aed8592701d77c8491c70e5414438224f582c1fb?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:3QyoC6OvQUmpQwQZ18iaTs"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/28ot3wh4oNmoFOdVajibBl"
                  },
                  "href": "https://api.spotify.com/v1/artists/28ot3wh4oNmoFOdVajibBl",
                  "id": "28ot3wh4oNmoFOdVajibBl",
                  "name": "NMIXX",
                  "type": "artist",
                  "uri": "spotify:artist:28ot3wh4oNmoFOdVajibBl"
                }
              ],
              "available_markets": [
                "AD",
                "AE",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BH",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IN",
                "IS",
                "IT",
                "JO",
                "KW",
                "LB",
                "LI",
                "LT",
                "LU",
                "LV",
                "MA",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PH",
                "PL",
                "PS",
                "PT",
                "PY",
                "QA",
                "RO",
                "SA",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TN",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/3AUtpZi3kqsEYDyQ0CCNiH"
              },
              "href": "https://api.spotify.com/v1/albums/3AUtpZi3kqsEYDyQ0CCNiH",
              "id": "3AUtpZi3kqsEYDyQ0CCNiH",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b2738d64ee7e356e13a96062bd0b",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e028d64ee7e356e13a96062bd0b",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d000048518d64ee7e356e13a96062bd0b",
                  "width": 64
                }
              ],
              "name": "AD MARE",
              "release_date": "2022-02-22",
              "release_date_precision": "day",
              "total_tracks": 4,
              "type": "album",
              "uri": "spotify:album:3AUtpZi3kqsEYDyQ0CCNiH"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/28ot3wh4oNmoFOdVajibBl"
                },
                "href": "https://api.spotify.com/v1/artists/28ot3wh4oNmoFOdVajibBl",
                "id": "28ot3wh4oNmoFOdVajibBl",
                "name": "NMIXX",
                "type": "artist",
                "uri": "spotify:artist:28ot3wh4oNmoFOdVajibBl"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NO",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "disc_number": 1,
            "duration_ms": 172936,
            "explicit": false,
            "external_ids": {
              "isrc": "US5TA2100138"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/3lrNsPdn98i6rxO142pLT6"
            },
            "href": "https://api.spotify.com/v1/tracks/3lrNsPdn98i6rxO142pLT6",
            "id": "3lrNsPdn98i6rxO142pLT6",
            "is_local": false,
            "name": "O.O",
            "popularity": 70,
            "preview_url": "https://p.scdn.co/mp3-preview/9e8d4c80ab6fdd85c35d90b2c0f4175561e861b9?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 2,
            "type": "track",
            "uri": "spotify:track:3lrNsPdn98i6rxO142pLT6"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/5fa13NJjmn2uQ3dxZDi2Ge"
                  },
                  "href": "https://api.spotify.com/v1/artists/5fa13NJjmn2uQ3dxZDi2Ge",
                  "id": "5fa13NJjmn2uQ3dxZDi2Ge",
                  "name": "Bich Phuong",
                  "type": "artist",
                  "uri": "spotify:artist:5fa13NJjmn2uQ3dxZDi2Ge"
                }
              ],
              "available_markets": [],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/0JoA8Z6TWI31c6uWXldxyU"
              },
              "href": "https://api.spotify.com/v1/albums/0JoA8Z6TWI31c6uWXldxyU",
              "id": "0JoA8Z6TWI31c6uWXldxyU",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b2734ff4ae8820513dc663f1006a",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e024ff4ae8820513dc663f1006a",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d000048514ff4ae8820513dc663f1006a",
                  "width": 64
                }
              ],
              "name": "tâm trạng tan hơi chậm một chút",
              "release_date": "2018-03-01",
              "release_date_precision": "day",
              "total_tracks": 4,
              "type": "album",
              "uri": "spotify:album:0JoA8Z6TWI31c6uWXldxyU"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/5fa13NJjmn2uQ3dxZDi2Ge"
                },
                "href": "https://api.spotify.com/v1/artists/5fa13NJjmn2uQ3dxZDi2Ge",
                "id": "5fa13NJjmn2uQ3dxZDi2Ge",
                "name": "Bich Phuong",
                "type": "artist",
                "uri": "spotify:artist:5fa13NJjmn2uQ3dxZDi2Ge"
              }
            ],
            "available_markets": [],
            "disc_number": 1,
            "duration_ms": 216000,
            "explicit": false,
            "external_ids": {
              "isrc": "VNA0M1907690"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/2IDZxVWQypWxYIP6wqDzGN"
            },
            "href": "https://api.spotify.com/v1/tracks/2IDZxVWQypWxYIP6wqDzGN",
            "id": "2IDZxVWQypWxYIP6wqDzGN",
            "is_local": false,
            "name": "em bỏ hút thuốc chưa",
            "popularity": 0,
            "preview_url": null,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:2IDZxVWQypWxYIP6wqDzGN"
          },
          {
            "album": {
              "album_type": "SINGLE",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/2xK6qcvfXuFFbU0NL95aeo"
                  },
                  "href": "https://api.spotify.com/v1/artists/2xK6qcvfXuFFbU0NL95aeo",
                  "id": "2xK6qcvfXuFFbU0NL95aeo",
                  "name": "Thịnh Suy",
                  "type": "artist",
                  "uri": "spotify:artist:2xK6qcvfXuFFbU0NL95aeo"
                }
              ],
              "available_markets": [
                "AD",
                "AE",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BH",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IN",
                "IS",
                "IT",
                "JO",
                "JP",
                "KW",
                "LB",
                "LI",
                "LT",
                "LU",
                "LV",
                "MA",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PH",
                "PL",
                "PS",
                "PT",
                "PY",
                "QA",
                "RO",
                "SA",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TN",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/19G96aFkB9NB2QrAVJPaCC"
              },
              "href": "https://api.spotify.com/v1/albums/19G96aFkB9NB2QrAVJPaCC",
              "id": "19G96aFkB9NB2QrAVJPaCC",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b273e425514244f161ea4ecb0d2a",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e02e425514244f161ea4ecb0d2a",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d00004851e425514244f161ea4ecb0d2a",
                  "width": 64
                }
              ],
              "name": "Nghe Em",
              "release_date": "2019-10-31",
              "release_date_precision": "day",
              "total_tracks": 1,
              "type": "album",
              "uri": "spotify:album:19G96aFkB9NB2QrAVJPaCC"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/2xK6qcvfXuFFbU0NL95aeo"
                },
                "href": "https://api.spotify.com/v1/artists/2xK6qcvfXuFFbU0NL95aeo",
                "id": "2xK6qcvfXuFFbU0NL95aeo",
                "name": "Thịnh Suy",
                "type": "artist",
                "uri": "spotify:artist:2xK6qcvfXuFFbU0NL95aeo"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "JP",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NO",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "disc_number": 1,
            "duration_ms": 268591,
            "explicit": false,
            "external_ids": {
              "isrc": "QMBZ91980712"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/5WHuqG7vz4Hy0BU47fPpVp"
            },
            "href": "https://api.spotify.com/v1/tracks/5WHuqG7vz4Hy0BU47fPpVp",
            "id": "5WHuqG7vz4Hy0BU47fPpVp",
            "is_local": false,
            "name": "Nghe Em",
            "popularity": 44,
            "preview_url": "https://p.scdn.co/mp3-preview/3ea0f3bd8e6873aa6b2e3be0259675c4e173259a?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:5WHuqG7vz4Hy0BU47fPpVp"
          },
          {
            "album": {
              "album_type": "ALBUM",
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/0BezPR1Hn38i8qShQKunSD"
                  },
                  "href": "https://api.spotify.com/v1/artists/0BezPR1Hn38i8qShQKunSD",
                  "id": "0BezPR1Hn38i8qShQKunSD",
                  "name": "Zhou Shen",
                  "type": "artist",
                  "uri": "spotify:artist:0BezPR1Hn38i8qShQKunSD"
                }
              ],
              "available_markets": [
                "AD",
                "AE",
                "AR",
                "AT",
                "AU",
                "BE",
                "BG",
                "BH",
                "BO",
                "BR",
                "CA",
                "CH",
                "CL",
                "CO",
                "CR",
                "CY",
                "CZ",
                "DE",
                "DK",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "ES",
                "FI",
                "FR",
                "GB",
                "GR",
                "GT",
                "HK",
                "HN",
                "HU",
                "ID",
                "IE",
                "IL",
                "IN",
                "IS",
                "IT",
                "JO",
                "JP",
                "KW",
                "LB",
                "LI",
                "LT",
                "LU",
                "LV",
                "MA",
                "MC",
                "MT",
                "MX",
                "MY",
                "NI",
                "NL",
                "NO",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PH",
                "PL",
                "PS",
                "PT",
                "PY",
                "QA",
                "RO",
                "SA",
                "SE",
                "SG",
                "SK",
                "SV",
                "TH",
                "TN",
                "TR",
                "TW",
                "US",
                "UY",
                "VN",
                "ZA"
              ],
              "external_urls": {
                "spotify": "https://open.spotify.com/album/6rXktEEIKU4LrdseMPzwaP"
              },
              "href": "https://api.spotify.com/v1/albums/6rXktEEIKU4LrdseMPzwaP",
              "id": "6rXktEEIKU4LrdseMPzwaP",
              "images": [
                {
                  "height": 640,
                  "url": "https://i.scdn.co/image/ab67616d0000b273bf24352caf35d83d05519573",
                  "width": 640
                },
                {
                  "height": 300,
                  "url": "https://i.scdn.co/image/ab67616d00001e02bf24352caf35d83d05519573",
                  "width": 300
                },
                {
                  "height": 64,
                  "url": "https://i.scdn.co/image/ab67616d00004851bf24352caf35d83d05519573",
                  "width": 64
                }
              ],
              "name": "深的深",
              "release_date": "2017-11-06",
              "release_date_precision": "day",
              "total_tracks": 10,
              "type": "album",
              "uri": "spotify:album:6rXktEEIKU4LrdseMPzwaP"
            },
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/0BezPR1Hn38i8qShQKunSD"
                },
                "href": "https://api.spotify.com/v1/artists/0BezPR1Hn38i8qShQKunSD",
                "id": "0BezPR1Hn38i8qShQKunSD",
                "name": "Zhou Shen",
                "type": "artist",
                "uri": "spotify:artist:0BezPR1Hn38i8qShQKunSD"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "JP",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NO",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "disc_number": 1,
            "duration_ms": 317597,
            "explicit": false,
            "external_ids": {
              "isrc": "CNZ021600012"
            },
            "external_urls": {
              "spotify": "https://open.spotify.com/track/0FfdtQrD9kT42o6Anv4uDn"
            },
            "href": "https://api.spotify.com/v1/tracks/0FfdtQrD9kT42o6Anv4uDn",
            "id": "0FfdtQrD9kT42o6Anv4uDn",
            "is_local": false,
            "name": "大魚 - 唱片版",
            "popularity": 53,
            "preview_url": "https://p.scdn.co/mp3-preview/e1ac88c9e6ceed0058b4449723c2c146b5ce9c44?cid=774b29d4f13844c495f206cafdad9c86",
            "track_number": 9,
            "type": "track",
            "uri": "spotify:track:0FfdtQrD9kT42o6Anv4uDn"
          }
        ],
        "total": 50,
        "limit": 10,
        "offset": 0,
        "href": "https://api.spotify.com/v1/me/top/tracks?limit=10&offset=0&time_range=long_term",
        "next": "https://api.spotify.com/v1/me/top/tracks?limit=10&offset=10&time_range=long_term",
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