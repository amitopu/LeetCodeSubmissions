class Solution:
    def simplifyPath(self, path: str) -> str:
        
        pathlist = path.split('/')
        stack = []
        stack.append('')
        for path in pathlist:
            
            if path == '..':
                if stack[-1] != '':
                    stack.pop()
            elif path != '.' and path != '':
                stack.append(path)
        
        if stack[-1] == '':
            return '/'
        
        result = '/'.join(stack)
        return result