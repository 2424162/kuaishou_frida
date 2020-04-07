#c.a.a(cls)

import frida, sys

# .overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String', 'java.lang.String')
jscode = '''
Java.perform(function () {
    console.log("kaishi")
    var c = Java.use('com.yxcorp.retrofit.f');

    c.a.overload('okhttp3.Request', 'java.util.Map', 'java.util.Map', 'java.lang.String').implementation = function (str1,str2,str3,str4) {
    var re = this.a(str1,str2,str3,str4) ;str1,str2,str3,str4
    //console.log();
    console.log(str1);
    console.log("____");
    console.log(str2);
    console.log("____");
    console.log(str3);
    console.log("-----");
    console.log(str4);

      




    }
});
'''


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_remote_device()  # .attach("com.smile.gifmaker")
process = process.attach('com.smile.gifmaker')
script = process.create_script(jscode)
script.on("message", on_message)
script.load()
sys.stdin.read()