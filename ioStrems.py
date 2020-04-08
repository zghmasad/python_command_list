import io

f = io.FileIO('test.xml')
br = io.BufferedReader(f)
print(br.read())

binary_stream_from_file =io.BufferedReader(io.BytesIO(b'starship.png'))
bytes = binary_stream_from_file.read(4)
print(bytes,'\n')

f = io.FileIO('test.xml')
br = io.BufferedReader(f)
text_stream = io.TextIOWrapper(br, 'utf-8')
print('text_stream.readable():', text_stream.readable())
print('text_stream.seekable()', text_stream.seekable())
print('text_stream.writeable()', text_stream.writable())
print(text_stream.read())
text_stream.close()




in_memory_text_stream = io.StringIO('to be or not to be that is the question')
print('in_memory_text_stream', in_memory_text_stream)
print(in_memory_text_stream.getvalue())
in_memory_text_stream.close()

print()

