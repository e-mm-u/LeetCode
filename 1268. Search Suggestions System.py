class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        def search(pre):
            l = len(pre)
            
            count = 0
            out = []
            for i in products:
                
                if pre==i[:l]:
                    out.append(i)
                    count += 1
                if count==3:
                    break
            
            return out


        output = []
        for i in range(len(searchWord)):
            pre = searchWord[:i+1]
            out = search(pre)
            output.append(out)
        
        return output
