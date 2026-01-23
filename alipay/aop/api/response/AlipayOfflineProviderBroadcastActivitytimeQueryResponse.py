#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpeakerActivityItem import SpeakerActivityItem


class AlipayOfflineProviderBroadcastActivitytimeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderBroadcastActivitytimeQueryResponse, self).__init__()
        self._page_size = None
        self._speaker_activity_list = None
        self._total_count = None

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def speaker_activity_list(self):
        return self._speaker_activity_list

    @speaker_activity_list.setter
    def speaker_activity_list(self, value):
        if isinstance(value, list):
            self._speaker_activity_list = list()
            for i in value:
                if isinstance(i, SpeakerActivityItem):
                    self._speaker_activity_list.append(i)
                else:
                    self._speaker_activity_list.append(SpeakerActivityItem.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderBroadcastActivitytimeQueryResponse, self).parse_response_content(response_content)
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'speaker_activity_list' in response:
            self.speaker_activity_list = response['speaker_activity_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
