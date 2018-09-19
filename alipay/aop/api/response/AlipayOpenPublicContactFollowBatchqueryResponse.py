#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ContactFollower import ContactFollower


class AlipayOpenPublicContactFollowBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicContactFollowBatchqueryResponse, self).__init__()
        self._contact_follow_list = None

    @property
    def contact_follow_list(self):
        return self._contact_follow_list

    @contact_follow_list.setter
    def contact_follow_list(self, value):
        if isinstance(value, list):
            self._contact_follow_list = list()
            for i in value:
                if isinstance(i, ContactFollower):
                    self._contact_follow_list.append(i)
                else:
                    self._contact_follow_list.append(ContactFollower.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicContactFollowBatchqueryResponse, self).parse_response_content(response_content)
        if 'contact_follow_list' in response:
            self.contact_follow_list = response['contact_follow_list']
