#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserGroupshoppingBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserGroupshoppingBenefitQueryResponse, self).__init__()
        self._amount = None
        self._have_benefit = None
        self._icon = None
        self._link = None
        self._reason = None
        self._sub_title = None
        self._title = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def have_benefit(self):
        return self._have_benefit

    @have_benefit.setter
    def have_benefit(self, value):
        self._have_benefit = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def sub_title(self):
        return self._sub_title

    @sub_title.setter
    def sub_title(self, value):
        self._sub_title = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserGroupshoppingBenefitQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'have_benefit' in response:
            self.have_benefit = response['have_benefit']
        if 'icon' in response:
            self.icon = response['icon']
        if 'link' in response:
            self.link = response['link']
        if 'reason' in response:
            self.reason = response['reason']
        if 'sub_title' in response:
            self.sub_title = response['sub_title']
        if 'title' in response:
            self.title = response['title']
