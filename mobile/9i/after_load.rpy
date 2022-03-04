label after_load:

    python hide:
        for node in renpy.ast.default_statements:
            d = renpy.python.store_dicts[node.store]
            
            if node.varname in d: continue
            
            d[node.varname] = renpy.python.py_eval_bytecode(node.code.bytecode)
            d.ever_been_changed.add(node.varname)

    stop movie


    if renpy.has_label("after_load_9i"):
        call after_load_9i from call_after_load_9i
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
