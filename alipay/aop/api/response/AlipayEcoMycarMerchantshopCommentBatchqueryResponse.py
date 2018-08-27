#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantshopCommentResult import MerchantshopCommentResult
from alipay.aop.api.domain.MerchantshopCommentStatistic import MerchantshopCommentStatistic


class AlipayEcoMycarMerchantshopCommentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarMerchantshopCommentBatchqueryResponse, self).__init__()
        self._comment_result = None
        self._comment_statistic = None

    @property
    def comment_result(self):
        return self._comment_result

    @comment_result.setter
    def comment_result(self, value):
        if isinstance(value, list):
            self._comment_result = list()
            for i in value:
                if isinstance(i, MerchantshopCommentResult):
                    self._comment_result.append(i)
                else:
                    self._comment_result.append(MerchantshopCommentResult.from_alipay_dict(i))
    @property
    def comment_statistic(self):
        return self._comment_statistic

    @comment_statistic.setter
    def comment_statistic(self, value):
        if isinstance(value, MerchantshopCommentStatistic):
            self._comment_statistic = value
        else:
            self._comment_statistic = MerchantshopCommentStatistic.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarMerchantshopCommentBatchqueryResponse, self).parse_response_content(response_content)
        if 'comment_result' in response:
            self.comment_result = response['comment_result']
        if 'comment_statistic' in response:
            self.comment_statistic = response['comment_statistic']
