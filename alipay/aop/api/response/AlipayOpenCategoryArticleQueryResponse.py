#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeRecommendArticles import LifeRecommendArticles


class AlipayOpenCategoryArticleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenCategoryArticleQueryResponse, self).__init__()
        self._articles = None

    @property
    def articles(self):
        return self._articles

    @articles.setter
    def articles(self, value):
        if isinstance(value, list):
            self._articles = list()
            for i in value:
                if isinstance(i, LifeRecommendArticles):
                    self._articles.append(i)
                else:
                    self._articles.append(LifeRecommendArticles.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenCategoryArticleQueryResponse, self).parse_response_content(response_content)
        if 'articles' in response:
            self.articles = response['articles']
