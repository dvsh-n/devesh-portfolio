import { readFileSync } from 'node:fs';

// GIF delays are stored in hundredths of a second. Browsers commonly display
// missing or extremely short delays as 100 ms.
export function gifDuration(path: string): number {
  const data = readFileSync(path);
  if (!/^GIF8[79]a$/.test(data.toString('ascii', 0, 6))) {
    throw new Error(`Invalid GIF: ${path}`);
  }
  let offset = 13;
  if (data[10] & 0x80) offset += 3 * (2 ** ((data[10] & 7) + 1));
  let delay = 100;
  let duration = 0;
  const skipBlocks = () => {
    while (offset < data.length) {
      const length = data[offset++];
      if (!length) return;
      offset += length;
    }
    throw new Error(`Truncated GIF: ${path}`);
  };
  while (offset < data.length) {
    const marker = data[offset++];
    if (marker === 0x3b) return duration || 100;
    if (marker === 0x21) {
      const label = data[offset++];
      if (label === 0xf9) {
        if (data[offset] !== 4) throw new Error(`Invalid GIF control block: ${path}`);
        const milliseconds = data.readUInt16LE(offset + 2) * 10;
        delay = milliseconds > 10 ? milliseconds : 100;
      }
      skipBlocks();
    } else if (marker === 0x2c) {
      const packed = data[offset + 8];
      offset += 9;
      if (packed & 0x80) offset += 3 * (2 ** ((packed & 7) + 1));
      offset++; // LZW minimum code size.
      skipBlocks();
      duration += delay;
      delay = 100;
    } else {
      throw new Error(`Unexpected GIF block in ${path}`);
    }
  }
  throw new Error(`Truncated GIF: ${path}`);
}
