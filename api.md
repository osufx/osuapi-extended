# osu!api - Extended

## http://github.com/osufx/osuapi-extended

## For API Version 0.2

### Overview
| Endpoint | Info | Read more |
| -------- | ---- | --------- |
| api/getDifficulty | Get calculated star rating of any map file that is publicly available | [getDifficulty](#getDifficulty) |
| api/getHash | Get body and header hash from a beatmap set | [getHash](#getHash) |

### getDifficulty
| Parameter | Info | Default | Required |
| --------- | ---- | ------- | -------- |
| c | md5 hash of the beatmap | None | Yes |

### getHash
| Parameter | Info | Default | Required |
| --------- | ---- | ------- | -------- |
| s | beatmapSetID for the beatmap | None | Yes |
##### info
This is not used anymore but early on in osu!'s life it used this to check if the local beatmap was outdated. (This is done elsewhere and differently now adays)