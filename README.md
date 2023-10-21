# Helpful (or not really) scripts

## Instalation

1. Clone the project:

```
git clone git@github.com:iaah04/helpful-scripts.git
```

## Usage like your own command

You can create a little scripts, just follow this instruction.
I will use password_generator for example:

1. Go to the folder with script and open file
2. Add shebang in the beginning of the file: #!/usr/bin/env python
3. Add to execute file: 

```
chmod +x generatepassword.py
```

4. Remove the extension of the file: 

```
mv generatepassword.py generatepassword
```

5. Move it to /usr/local/bin: 

```
mv ./generatepassword /usr/local/bin
```

6. Open terminal and use it:

```
generatepassword
```

Tnx [this](https://pythobyte.com/create-custom-terminal-command-1dr0yhg33s-eef956b2/) guide 🖤

## Usage with virtual enviroment

If you don't want to download python libraries globally, you can use virtual environment.
I will use simple_steganography for example:

1. Choose folder for virtual enviroment, for example simple_steganography.

2. Create virtual enviroment with the next command:

```
virtualenv name
```

3. Activate it:

On Windows:

```
.\name\Scripts\activate
```

On macOS and Linux:

```
source name/bin/activate
```

After that you can download libraries and they will be available for scripts.

4. For deactivation:

```
deactivate
```
