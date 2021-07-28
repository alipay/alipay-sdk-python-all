#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ArticleInfo import ArticleInfo


class AlipayIserviceCcmSwArticleBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwArticleBatchqueryResponse, self).__init__()
        self._articles = None

    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, value):
        if isinstance(value, list):
            self._articles = list()
            for i in value:
                if isinstance(i, ArticleInfo):
                    self._articles.append(i)
                else:
                    self._articles.append(ArticleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwArticleBatchqueryResponse, self).parse_response_content(response_content)
        if 'articles' in response:
            self.articles = response['articles']
