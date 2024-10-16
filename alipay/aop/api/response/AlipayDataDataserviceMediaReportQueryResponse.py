#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MediaReportDetail import MediaReportDetail


class AlipayDataDataserviceMediaReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceMediaReportQueryResponse, self).__init__()
        self._m_pid = None
        self._m_pid_name = None
        self._media_report_data_list = None
        self._page_no = None
        self._page_size = None
        self._pid = None
        self._total = None

    @property
    def m_pid(self):
        return self._m_pid

    @m_pid.setter
    def m_pid(self, value):
        self._m_pid = value
    @property
    def m_pid_name(self):
        return self._m_pid_name

    @m_pid_name.setter
    def m_pid_name(self, value):
        self._m_pid_name = value
    @property
    def media_report_data_list(self):
        return self._media_report_data_list

    @media_report_data_list.setter
    def media_report_data_list(self, value):
        if isinstance(value, list):
            self._media_report_data_list = list()
            for i in value:
                if isinstance(i, MediaReportDetail):
                    self._media_report_data_list.append(i)
                else:
                    self._media_report_data_list.append(MediaReportDetail.from_alipay_dict(i))
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceMediaReportQueryResponse, self).parse_response_content(response_content)
        if 'm_pid' in response:
            self.m_pid = response['m_pid']
        if 'm_pid_name' in response:
            self.m_pid_name = response['m_pid_name']
        if 'media_report_data_list' in response:
            self.media_report_data_list = response['media_report_data_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'pid' in response:
            self.pid = response['pid']
        if 'total' in response:
            self.total = response['total']
