import re
def format_input(input_str):
    lines = input_str.split('\n')
    formatted_lines = []
    for line in lines:
        cleaned_line = re.sub(r'\s+', ' ', line.strip())
        formatted_line = re.sub(r'(\blabel\d+)\s+', r'\1 ', cleaned_line)
        formatted_lines.append(formatted_line)
    formatted_str = '\n'.join(formatted_lines)
    return formatted_str


def binary_to_hex(binary_string):
    decimal_num = int(binary_string, 2)
    hex_string = hex(decimal_num).upper()
    return hex_string

def hex_addition(hex1, hex2):
    dec1 = int(hex1, 16)
    dec2 = int(hex2, 16)
    result_dec = dec1 + dec2
    result_hex = hex(result_dec).upper()
    return result_hex

def hexadecimal_subtraction(hex_str1, hex_str2):
    num1 = int(hex_str1, 16)
    num2 = int(hex_str2, 16)
    result = num1 - num2
    if result < 0:
        result += 0x100000000  
    result_hex = hex(result)
    return result_hex





def compile(code):
    optab = {
        'ADD': '18','ADDF':'18','ADDR':'90','AND':'40','CLEAR':'B4',
        'COMP':'28','COMPF':'88','COMPR':'2','DIV':'24','DIVF':'64',
        'DIVR':'2','FIX':'1','FLOAT':'1','HIO':'1','J':'3C','JEQ':'30',
        'JGT':'34','JLT':'38','JSUB':'48','LDA':'00','LDB':'68','LDCH':'50',
        'LDF':'70','LDL':'08','LDS':'6C','LDT':'74','LDX':'04','LPS':'D0',
        'MUL':'20','MULF':'60','MULR':'98','NORM':'C8','OR':'44','RD':'D8',
        'RMO':'AC','RSUB':'4C','SHIFTL':'A4','SHIFTR':'A8','SIO':'F0',
        'SSK':'EC','STA':'0C','STB':'78','STCH':'54','STF':'80','STI':'D4',
        'STL':'14','STS':'7C','STSW':'E8','STT':'84','STX':'10','SUB':'1C',
        'SUBF':'5C','SUBR':'94','SVC':'B0','TID':'E0','TIO':'F8','TIX':'2C',
        'TIXR':'B8','WD':'DC'
    }
    
    memonic={'NUL':'00','SOH':'01','STX':'02','ETX':'03','EOT':'04','ENQ':'05',
             'ACK':'06','BEL':'07','BS':'08','HT':'09','LF':'0A','VT':'0B',
             'FF':'0C','CR':'0D','S0':'0E','SI':'0F','DLE':'10','DC1':'11',
             'DC2':'12','DC3':'13','DC4':'14','NAK':'15','SYN':'16','ETB':'17',
             'CAN':'18','EM':'19','SUB':'1A','ESC':'1B','FS':'1C','GS':'1D',
             'RS':'1E','US':'1F','SP':'20','!':'21','"':'22','#':'23','$':'24',
             '%':'25','&':'26',"'":'27','(':'28',')':'29','*':'2A','+':'2B',',':'2C',
             '-':'2D','.':'2E','/':'2F','0':'30','1':'31','2':'32','3':'33','4':'34',
             '5':'35','6':'36','7':'37','8':'38','9':'39',':':'3A',';':'3B','<':'3C',
             '=':'3D','>':'3E','?':'3F','@':'40','A':'41','B':'42','C':'43','D':'44',
             'E':'45','F':'46','G':'47','H':'48','I':'49','J':'4A','K':'4B','L':'4C',
             'M':'4D','N':'4E','O':'4F','P':'50','Q':'51','R':'52','S':'53','T':'54',
             'U':'55','V':'56','W':'57','X':'58','Y':'59','Z':'5A','[':'5B','\\':'5C',
             ']':'5D','^':'5E','_':'5F','`':'60','a':'61','b':'62','c':'63','d':'64',
             'e':'65','f':'66','g':'67','h':'68','i':'69','j':'6A','k':'6B','l':'6C',
             'm':'6D','n':'6E','o':'6F','p':'70','q':'71','r':'72','s':'73','t':'74',
             'u':'75','v':'76','w':'77','x':'78','y':'79','z':'7A','{':'7B','|':'7C',
             '}':'7D','~':'7E','DEL':'7F'
    }
    
    registers={'A':'0','X':'1','L':'2','PC':'8','SW':'9','B':'3','S':'4','T':'5','F':'6'}
    reg=[]
    x1=''
    symtab = {}
    syntab_output = ""
    code=format_input(code)
    result= ""
    output1 = ""
    lines = code.strip().split("\n")
    label, opcode, operand = lines[0].split(" ")
    locctr = 0
    index = 1
    final_result=''
    result += "Output:\n"
    result+="LOCCTR\t\tLABEL\t\tOPCODE\t\tOPRERAND\n"
    if opcode == "START":
        start = int(operand)
        locctr = hex_addition(str(locctr),str(start))[2:]
        result+= f"{locctr}\t\t\t{label}\t\t\t{opcode}\t\t{operand}\n"
        label, opcode, operand = lines[index].split(" ")
        index += 1

    while opcode != "END":
        if '+' in opcode:
            opcode=opcode.replace('+','')
            x1='+'
        result+= f"{locctr}\t\t\t\t"
        if label != "**":
            symtab[label] = locctr

        if label != "**":
           result+= f"{label}\t\t"
        else:
           result+= "**\t\t\t"
        print(locctr)
        if x1=='+':
            locctr =hex_addition(locctr,'4')[2:]
            result+= f"{x1}{opcode}\t\t\t{operand}\n"
        elif opcode=='ADDR' or opcode=='CLEAR' or opcode=='COMPR' or opcode=='DIVR' or opcode=='MULR' or opcode=='RMO' or opcode=='SHIFTL' or opcode=='SHIFTR' or opcode=='SUBR' or opcode=='SVC' or opcode=='TIXR':
            locctr =hex_addition(locctr,'2')[2:]
            result+= f"{x1}{opcode}\t\t\t{operand}\n"
        else:
            if opcode in optab:
                locctr =hex_addition(locctr,'3')[2:]
                result+= f"{x1}{opcode}\t\t\t{operand}\n"
            elif opcode == "WORD":
                locctr =hex_addition(locctr,'3')[2:]
                result+= f"{x1}{opcode}\t\t\t{operand}\n"
            elif opcode == "RESW":
                locctr =hex_addition(locctr,str(hex(3*int(operand))))[2:]
                result+= f"{x1}{opcode}\t\t\t{operand}\n"
            elif opcode == "RESB":
                locctr =hex_addition(locctr,operand)[2:]
                result+= f"{1}{opcode}\t\t\t{operand}\n"
            elif opcode == "BYTE":
                locctr=hex_addition(locctr,str(len(operand)-3))[2:]
                result+= f"{x1}{opcode}\t\t\t{operand}\n"

        label, opcode, operand = lines[index].split(" ")
        index += 1
        x1=''
    result+= f"{locctr}\t\t{label}\t\t\t{x1}{opcode}\t\t\t{operand}\n"
    length = hexadecimal_subtraction(locctr,str(start))
    result += f"\nlength of the code : {length}\n"

    symtab_str = "\n".join([f"{key}\t{value}" for key, value in symtab.items()])
    output = "Symbol Table:\nLABEL\tLOCCTR\n"+symtab_str + "\n\n" + result
    print(output)
    
    
    y,z=result,symtab_str
    pass1 = y.split('\n')[2:]
    pass2=pass1[:len(pass1)-3]
    syntab=z.split('\n')
    for line in syntab:
        if line.strip():  # check if line is not empty
            syntab_output += "\t".join(line.split()) + "\n"
        else:
            syntab_output += "\n"
    syntab=format_input(syntab_output)
    syntab=syntab.split('\n')
    syntab=syntab[:len(syntab)-1]
    
    
    for line in pass2:
        if line.strip():  # check if line is not empty
            output1 += "\t".join(line.split()) + "\n"
        else:
            output1 += "\n"
    pass2=format_input(output1)
    pass2=pass2.split("\n")
    x1=''
    index=0
    locctr ,label, opcode, operand = pass2[index].split(" ")
    n,i,x,b,p,e=0,0,0,0,0,0
    if opcode == "START":
        start = '**'
        obj_code = start.upper()
        final_result+= f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t{operand}\t\t{obj_code}\n"
    index=1
    locctr ,label, opcode, operand = pass2[index].split(" ")
    while opcode!='END':
        obj_code=''
        if '+' in opcode:
            opcode=opcode.replace('+','')
            x1='+'
            
        if opcode == 'RESW' or opcode == 'RESB' or opcode == 'WORD':
            obj_code='**'
            final_result+=f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t{operand}\t\t{obj_code}\n"
        
        elif opcode == 'BYTE':
            if operand[0]=='C':
                value=operand[2:len(operand)-1]
                for i in value:
                    obj_code+=memonic[i]
            elif operand[0]=='X':
                obj_code+=operand[2:len(operand)-1]
                
            final_result+=f"{locctr}\t\t\t{label}\t\t{opcode}\t\t{operand}\t\t{obj_code}\n"
        
        elif opcode == 'BYTE':
            
            if operand[0]=='C':
                value=operand[2:len(operand)-1]
                for i in value:
                    obj_code+=memonic[i].upper()
                    
            elif operand[0]=='X':
                obj_code+=operand[2:len(operand)-1].upper()
            final_result+=f"{locctr}\t\t\t{label}\t\t{x1}{opcode}\t\t{operand}\t\t{obj_code}\n"
        
        
        elif opcode=='ADDR' or opcode=='CLEAR' or opcode=='COMPR' or opcode=='DIVR' or opcode=='MULR' or opcode=='RMO' or opcode=='SHIFTL' or opcode=='SHIFTR' or opcode=='SUBR' or opcode=='SVC' or opcode=='TIXR':
            oper=operand.split(',')
            for i in range(len(oper)):
                decimal_num=bin(int(registers[oper[i]]))
                reg.append(binary_to_hex(decimal_num)[2:])
            if len(reg)<2:
                obj_code=f'{optab[opcode]}{reg[0]}0'.upper()
            else:
                obj_code=f'{optab[opcode]}{reg[0]}{reg[1]}'.upper()
            final_result+=f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t\t{operand}\t\t{obj_code}\n"
        
        
        else:

            if ('@' in operand):
                n,i,b,p,e=1,0,0,1,0
            elif ('#' in operand):
                n,i,b,p,e=0,1,0,1,0   
            else:
                n,i,b,p,e=1,1,0,1,0
            if 'x' in operand:
                x=1
            else:
                x=0
            if x1=='+':
                e,b,p=1,0,0
            else:
                e=0
            if operand=='#0':
                x,b,p,e=0,0,0,0
                
            
            hex_ni=binary_to_hex(f'000000{n}{i}')
            
            addr=hex_addition(optab[opcode],hex_ni)
            addr=addr[len(addr)-2:]
            addr=addr.replace('X','0')
            
            obj_code+=addr.upper()
            obj_code+=binary_to_hex(f'{x}{b}{p}{e}')[2:].upper()
            if '#' in operand and e==1:
                try:
                    disp=bin(int(operand.replace('#','')))[2:]
                    disp=binary_to_hex(disp)[2:]
                    print(disp)
                    if len(disp)==5:
                        obj_code+=disp.upper()
                    else:
                        obj_code+=f'0{disp}'.upper()
                    final_result+=f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t\t{operand}\t\t{obj_code}\n"
                
                except ValueError:
                    operand=operand.replace('#','')
                    op='#'
                    disp=locctr
                    for i in range(len(syntab)):
                        sym_label,sym_locctr=syntab[i].split(" ")
                        if sym_label == operand:
                            disp=sym_locctr
                    if len(disp)<5:
                        obj_code+=f'0{disp}'.upper()
                    else:
                        obj_code+=disp[len(disp)-5:].upper()
                    final_result+=f"{locctr}\t\t\t{label}\t\t{x1}{opcode}\t\t{operand}\t\t{obj_code}\n"
                    op=''
                
            elif '#' in operand:
                
                try:
                    disp=bin(int(operand.replace('#','')))[2:]
                    disp=binary_to_hex(disp)[2:]
                    if len(disp)==5:
                        obj_code+=disp.upper()
                    else:
                        obj_code+=f'0{disp}'.upper()
                    final_result+=f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t\t{operand}\t\t{obj_code}\n"
                    
                    
                    
                except ValueError:
                    operand=operand.replace('#','')
                    op='#'
                    disp=locctr
                    for i in range(len(syntab)):
                        sym_label,sym_locctr=syntab[i].split(" ")
                        if sym_label == operand:
                            disp=sym_locctr
                            
                            
                    index+=1
                    locctr ,label, opcode, operand = pass2[index].split(" ")
                    disp=hexadecimal_subtraction(disp,locctr)
                    disp=disp[len(disp)-3:].upper()
                    obj_code+=disp.replace('X','0')
                    index-=1
                    locctr ,label, opcode, operand = pass2[index].split(" ")
                    final_result+=f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t\t{operand}\t\t{obj_code}\n"
                    op=''
                    
            elif e==0:
                disp=locctr
                for i in range(len(syntab)):
                    sym_label,sym_locctr=syntab[i].split(" ")
                    if sym_label == operand:
                        disp=sym_locctr
                        
                index+=1
                locctr ,label, opcode, operand = pass2[index].split(" ")
                disp=hexadecimal_subtraction(disp,locctr)
                disp=disp[len(disp)-3:].upper()
                obj_code+=disp.replace('X','0')
                index-=1
                locctr ,label, opcode, operand = pass2[index].split(" ")
                final_result+=f"{locctr}\t\t\t{label}\t\t\t{opcode}\t\t\t{operand}\t\t{obj_code}\n"
            
            elif e==1:
                disp=locctr
                for i in range(len(syntab)):
                    sym_label,sym_locctr=syntab[i].split(" ")
                    if sym_label == operand:
                        disp=sym_locctr
                if len(disp)<5:
                    # print(disp)
                    obj_code+='0'*(5-int(len(disp)))
                    obj_code+=f'{disp}'.upper()
                else:
                    obj_code+=disp[len(disp)-5:].upper()
                final_result+=f"{locctr}\t\t\t{label}\t\t{x1}{opcode}\t\t{operand}\t\t{obj_code}\n"
            
        index+=1
        locctr ,label, opcode, operand = pass2[index].split(" ")
        if opcode=='END':
            obj_code='**'
        x1=''
        op=''
    final_result+=f"{locctr}\t\t\t{label}\t\t\t{x1}{opcode}\t\t\t{operand}\t\t{obj_code}\n"
    final_result= 'LOCCTR\t\t\tLABEL\t\tOPCODE\t\tOPERAND\tOBJECT CODE\n'+final_result
    final_result=format_input(final_result)
    return final_result