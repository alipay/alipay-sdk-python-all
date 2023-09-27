#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PromoActivityAccessActionVO import PromoActivityAccessActionVO
from alipay.aop.api.domain.PromoActivityAttrVO import PromoActivityAttrVO


class AlipayOpenAppItempromoactivityTemplateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItempromoactivityTemplateQueryResponse, self).__init__()
        self._access_action = None
        self._activity_attrs = None
        self._desc = None
        self._promotion_type = None
        self._proved = None
        self._reason = None
        self._title = None

    @property
    def access_action(self):
        return self._access_action

    @access_action.setter
    def access_action(self, value):
        if isinstance(value, PromoActivityAccessActionVO):
            self._access_action = value
        else:
            self._access_action = PromoActivityAccessActionVO.from_alipay_dict(value)
    @property
    def activity_attrs(self):
        return self._activity_attrs

    @activity_attrs.setter
    def activity_attrs(self, value):
        if isinstance(value, list):
            self._activity_attrs = list()
            for i in value:
                if isinstance(i, PromoActivityAttrVO):
                    self._activity_attrs.append(i)
                else:
                    self._activity_attrs.append(PromoActivityAttrVO.from_alipay_dict(i))
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value
    @property
    def proved(self):
        return self._proved

    @proved.setter
    def proved(self, value):
        self._proved = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItempromoactivityTemplateQueryResponse, self).parse_response_content(response_content)
        if 'access_action' in response:
            self.access_action = response['access_action']
        if 'activity_attrs' in response:
            self.activity_attrs = response['activity_attrs']
        if 'desc' in response:
            self.desc = response['desc']
        if 'promotion_type' in response:
            self.promotion_type = response['promotion_type']
        if 'proved' in response:
            self.proved = response['proved']
        if 'reason' in response:
            self.reason = response['reason']
        if 'title' in response:
            self.title = response['title']
