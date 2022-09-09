
# Message

## Structure

`Message`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `callback_url` | `string` | Optional | URL replies and delivery reports to this message will be pushed to |
| `content` | `string` | Required | Content of the message<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `5000` |
| `destination_number` | `string` | Required | Destination number of the message<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `15` |
| `delivery_report` | `bool` | Optional | Request a delivery report for this message<br>**Default**: `False` |
| `format` | [`List of FormatEnum`](../../doc/models/format-enum.md) | Optional | Format of message, SMS, MMS or TTS (Text To Speech). |
| `media` | `List of string` | Optional | - |
| `message_expiry_timestamp` | `datetime` | Optional | Date time after which the message expires and will not be sent |
| `metadata` | `object` | Optional | Metadata for the message specified as a set of key value pairs, each key can be up to 100 characters long and each value can be up to 256 characters long<br><br>```<br>{<br>   "myKey": "myValue",<br>   "anotherKey": "anotherValue"<br>}<br>``` |
| `scheduled` | `datetime` | Optional | Scheduled delivery date time of the message |
| `source_number` | `string` | Optional | - |
| `source_number_type` | [`SourceNumberTypeEnum`](../../doc/models/source-number-type-enum.md) | Optional | Type of source address specified, this can be INTERNATIONAL, ALPHANUMERIC or SHORTCODE |

## Example (as JSON)

```json
{
  "content": "Hello world!",
  "destination_number": "+61491570156"
}
```

