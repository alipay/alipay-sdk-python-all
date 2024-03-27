#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EntryHealthPersonInfo import EntryHealthPersonInfo


class AlipayDigitalmgmtHrhealthEntryUserBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtHrhealthEntryUserBatchqueryResponse, self).__init__()
        self._entry_person_list = None

    @property
    def entry_person_list(self):
        return self._entry_person_list

    @entry_person_list.setter
    def entry_person_list(self, value):
        if isinstance(value, list):
            self._entry_person_list = list()
            for i in value:
                if isinstance(i, EntryHealthPersonInfo):
                    self._entry_person_list.append(i)
                else:
                    self._entry_person_list.append(EntryHealthPersonInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtHrhealthEntryUserBatchqueryResponse, self).parse_response_content(response_content)
        if 'entry_person_list' in response:
            self.entry_person_list = response['entry_person_list']
