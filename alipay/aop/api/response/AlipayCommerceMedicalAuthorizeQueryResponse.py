#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAuthorizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAuthorizeQueryResponse, self).__init__()
        self._institution_ecode_status = None
        self._page_suggestion = None
        self._page_url = None
        self._status = None

    @property
    def institution_ecode_status(self):
        return self._institution_ecode_status

    @institution_ecode_status.setter
    def institution_ecode_status(self, value):
        self._institution_ecode_status = value
    @property
    def page_suggestion(self):
        return self._page_suggestion

    @page_suggestion.setter
    def page_suggestion(self, value):
        self._page_suggestion = value
    @property
    def page_url(self):
        return self._page_url

    @page_url.setter
    def page_url(self, value):
        self._page_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAuthorizeQueryResponse, self).parse_response_content(response_content)
        if 'institution_ecode_status' in response:
            self.institution_ecode_status = response['institution_ecode_status']
        if 'page_suggestion' in response:
            self.page_suggestion = response['page_suggestion']
        if 'page_url' in response:
            self.page_url = response['page_url']
        if 'status' in response:
            self.status = response['status']
