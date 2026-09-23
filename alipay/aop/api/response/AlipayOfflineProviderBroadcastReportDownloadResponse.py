#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderBroadcastReportDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderBroadcastReportDownloadResponse, self).__init__()
        self._download_url = None
        self._file_size = None
        self._report_dt = None
        self._status = None
        self._status_message = None
        self._task_id = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def report_dt(self):
        return self._report_dt

    @report_dt.setter
    def report_dt(self, value):
        self._report_dt = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_message(self):
        return self._status_message

    @status_message.setter
    def status_message(self, value):
        self._status_message = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderBroadcastReportDownloadResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'file_size' in response:
            self.file_size = response['file_size']
        if 'report_dt' in response:
            self.report_dt = response['report_dt']
        if 'status' in response:
            self.status = response['status']
        if 'status_message' in response:
            self.status_message = response['status_message']
        if 'task_id' in response:
            self.task_id = response['task_id']
