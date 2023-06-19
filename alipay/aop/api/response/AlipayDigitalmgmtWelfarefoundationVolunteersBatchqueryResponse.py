#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QueryVolunteersDto import QueryVolunteersDto


class AlipayDigitalmgmtWelfarefoundationVolunteersBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtWelfarefoundationVolunteersBatchqueryResponse, self).__init__()
        self._activity_hours = None
        self._result = None

    @property
    def activity_hours(self):
        return self._activity_hours

    @activity_hours.setter
    def activity_hours(self, value):
        if isinstance(value, list):
            self._activity_hours = list()
            for i in value:
                if isinstance(i, QueryVolunteersDto):
                    self._activity_hours.append(i)
                else:
                    self._activity_hours.append(QueryVolunteersDto.from_alipay_dict(i))
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtWelfarefoundationVolunteersBatchqueryResponse, self).parse_response_content(response_content)
        if 'activity_hours' in response:
            self.activity_hours = response['activity_hours']
        if 'result' in response:
            self.result = response['result']
