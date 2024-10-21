## Installation

Follow the steps below to install the necessary libraries and tools for the scraper.

### 1. Install the Required Python Packages

Run the following commands in your terminal to install the main packages needed for web scraping:

```bash
pip install xhs
```
This is the main package we will be using to interact with the Xiaohongshu API.

```bash
pip install playwright
```
Playwright is a browser automation tool that helps us interact with web pages programmatically.

### 2. Install Playwright Browsers

Playwright comes with its own browser binaries. Install them by running the following command:

```bash
playwright install
```

### 3. Download the Stealth Script

The `stealth.min.js` script helps to bypass anti-bot detection mechanisms on Xiaohongshu, making it easier for the scraper to avoid being blocked.

```bash
curl -O https://cdn.jsdelivr.net/gh/requireCool/stealth.min.js/stealth.min.js
```

### 4. Customize the Code

There are two places where you will need to personalize the script:

1. **Update the Path to `stealth.min.js`**:
   - In the `sign` function, update the `stealth_js_path` with the correct path to your `stealth.min.js` file:
     ```python
     stealth_js_path = "/path/to/your/stealth.min.js"
     ```

2. **Insert Your Cookie Values**:
   - In the `if __name__ == '__main__':` block, you will need to retrieve your `a1`, `web_session`, and `webId` cookies from Xiaohongshu and replace the placeholder:
     ```python
     cookie = "a1=your_a1_value; web_session=your_web_session_value; webId=your_webId_value"
     ```

### How to Retrieve Cookies from Xiaohongshu

#### 1. Open Xiaohongshu in Your Browser

   - Open your browser (Google Chrome or Firefox).
   - Navigate to [https://www.xiaohongshu.com](https://www.xiaohongshu.com) and log in to your account.

#### 2. Open Developer Tools

   - In Chrome: Right-click anywhere on the page and select **Inspect** or press `Ctrl + Shift + I` (Windows/Linux) or `Cmd + Option + I` (Mac).
   - In Firefox: Right-click and choose **Inspect** or press `F12`.

#### 3. Go to the "Application" or "Storage" Tab

   - In the developer tools panel, select the **Application** tab in Chrome or **Storage** tab in Firefox.
   - If it’s not visible, click the `>>` icon to reveal hidden tabs.

#### 4. Find Cookies

   - In the left sidebar, locate **Cookies** under the **Storage** or **Application** section.
   - Select the domain `xiaohongshu.com` to see all cookies related to Xiaohongshu.

#### 5. Locate the Required Cookies

   - Find the `a1`, `web_session`, and `webId` cookies.
   - Copy the **Value** of each cookie.

#### 6. Insert the Cookie Values in Your Script

   - Format the cookie string like this, ensuring that you use semicolons (`;`) to separate the cookies:
     ```python
     cookie = "a1=your_a1_value; web_session=your_web_session_value; webId=your_webId_value"
     ```

Now you can run your Python script with the correct cookie settings.

---


## 安装步骤

按照以下步骤安装爬虫所需的库和工具。

### 1. 安装所需的 Python 包

在终端中运行以下命令来安装爬取所需的主要包：

```bash
pip install xhs
```
这是与小红书 API 交互所用的主要包。

```bash
pip install playwright
```
Playwright 是一个浏览器自动化工具，用于编程方式与网页交互。

### 2. 安装 Playwright 浏览器

Playwright 自带浏览器二进制文件。运行以下命令来安装它们：

```bash
playwright install
```

### 3. 下载 Stealth 脚本

`stealth.min.js` 脚本帮助绕过小红书的反爬虫机制，使爬虫避免被封禁。

```bash
curl -O https://cdn.jsdelivr.net/gh/requireCool/stealth.min.js/stealth.min.js
```

### 4. 个性化代码

有两处代码需要根据您的环境进行修改：

1. **更新 `stealth.min.js` 路径**：
   - 在 `sign` 函数中，更新 `stealth_js_path` 为正确的 `stealth.min.js` 文件路径：
     ```python
     stealth_js_path = "/path/to/your/stealth.min.js"
     ```

2. **插入您的 Cookie 值**：
   - 在 `if __name__ == '__main__':` 块中，您需要从小红书获取 `a1`、`web_session` 和 `webId` Cookie，并替换占位符：
     ```python
     cookie = "a1=your_a1_value; web_session=your_web_session_value; webId=your_webId_value"
     ```

### 如何从小红书获取 Cookie

#### 1. 在浏览器中打开小红书

   - 打开您的浏览器（Google Chrome 或 Firefox）。
   - 访问 [https://www.xiaohongshu.com](https://www.xiaohongshu.com)，并登录您的账号。

#### 2. 打开开发者工具

   - 在 Chrome 中：右键点击页面任意位置，选择 **Inspect（检查）**，或按 `Ctrl + Shift + I`（Windows/Linux）或 `Cmd + Option + I`（Mac）。
   - 在 Firefox 中：右键点击页面，选择 **Inspect（检查）** 或按 `F12`。

#### 3. 转到 "Application" 或 "Storage" 标签

   - 在开发者工具面板中，选择 Chrome 的 **Application（应用）** 标签或 Firefox 的 **Storage（存储）** 标签。
   - 如果标签不可见，点击 `>>` 图标以显示隐藏的标签。

#### 4. 查找 Cookies

   - 在左侧栏中，定位到 **Cookies** 部分，位于 **Storage（存储）** 或 **Application（应用）** 下。
   - 选择域名 `xiaohongshu.com` 来查看与小红书相关的所有 cookies。

#### 5. 找到所需的 Cookies

   - 查找 `a1`、`web_session` 和 `webId` cookies。
   - 复制每个 cookie 的 **Value（值）**。

#### 6. 在代码中插入 Cookie 值

   - 按如下格式组织 cookie 字符串，确保使用分号（`;`）分隔 cookies：
     ```python
     cookie = "a1=your_a1_value; web_session=your_web_session_value; webId=your_webId_value"
     ```

现在，您可以运行带有正确 cookie 设置的 Python 脚本。

---
