#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayImgReviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayImgReviewQueryResponse, self).__init__()
        self._review_status = None

    @property
    def review_status(self):
        return self._review_status

    @review_status.setter
    def review_status(self, value):
        self._review_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayImgReviewQueryResponse, self).parse_response_content(response_content)
        if 'review_status' in response:
            self.review_status = response['review_status']
