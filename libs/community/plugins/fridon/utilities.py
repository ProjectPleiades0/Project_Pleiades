from libs.community.helpers.chains import create_retriever_chain
from pleiadesai_core.plugins.utilities import BaseUtility


class pleiadesRagUtility(BaseUtility):
    async def arun(self, question: str, *args, **kwargs) -> str:
        retrieval_chain = create_retriever_chain(
            "libs/community/plugins/pleiades/pleiades.md"
        )
        response = await retrieval_chain.ainvoke({"input": question})

        return response
