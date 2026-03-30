module.exports = {
  testEnvironment: 'node',
  testEnvironmentOptions: {
    localstoragePath: '/tmp/jest_localstorage'
  },
  collectCoverageFrom: [
    'src/**/*.js',
    '!src/index.js',
    '!src/**/*.test.js'
  ],
  testMatch: ['**/tests/**/*.test.js'],
  verbose: true
};
